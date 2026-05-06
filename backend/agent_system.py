from llm_client import call_llm
from code_executor import save_files, run_tests

# KDF SYSTEM
from kdf_loader import load_kdfs
from vector_store import search_kdfs
from kdf_to_code import generate_code_from_kdf


# -----------------------------------
# TEMPLATE FALLBACK (STABLE)
# -----------------------------------
def generate_template_code():
    return """
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional
import uuid

app = FastAPI()

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None


class Task(TaskCreate):
    id: str


tasks: Dict[str, Task] = {}


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())
    new_task = Task(id=task_id, **task.dict())
    tasks[task_id] = new_task
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = Task(id=task_id, **task.dict())
    tasks[task_id] = updated
    return updated


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}
"""


# -----------------------------------
# TEST TEMPLATE
# -----------------------------------
def generate_tests():
    return """
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create():
    r = client.post("/tasks", json={"title": "t1"})
    assert r.status_code == 201
"""


# -----------------------------------
# HELPERS
# -----------------------------------
def has_test_failures(output: str):
    output = output.lower()
    return any(x in output for x in [
        "failed", "error", "traceback", "assert", "exception"
    ])


def is_valid_code(code: str):
    return (
        "FastAPI" in code and
        "@app.post" in code and
        "def create_task" in code
    )


def fix_code_with_llm(error, code):
    prompt = f"""
Fix this FastAPI code.

RULES:
- DO NOT change API routes
- DO NOT remove functionality
- ONLY fix errors
- RETURN ONLY Python code

ERROR:
{error}

CODE:
{code}
"""
    return call_llm(prompt)


# -----------------------------------
# MAIN PIPELINE
# -----------------------------------
def execute_pipeline(query, context):

    # -----------------------------
    # STEP 1 — PLAN (OPTIONAL)
    # -----------------------------
    plan = ""
    if "build" in query.lower():
        plan = call_llm(f"Break into steps:\n{query}")

    # -----------------------------
    # STEP 2 — KDF SEARCH
    # -----------------------------
    try:
        kdfs, _ = load_kdfs()
        relevant = search_kdfs(query)
    except Exception as e:
        print("⚠️ KDF error:", e)
        relevant = []

    # -----------------------------
    # STEP 3 — CODE GEN
    # -----------------------------
    if relevant:
        print("🧠 Using KDF")
        try:
            code = generate_code_from_kdf(relevant[0])
        except Exception as e:
            print("⚠️ KDF failed → fallback")
            code = generate_template_code()
    else:
        print("⚠️ No KDF → template")
        code = generate_template_code()

    tests = generate_tests()

    save_files(code, tests)

    # -----------------------------
    # STEP 4 — TEST
    # -----------------------------
    test_output = run_tests()
    print("🧪 TEST OUTPUT:\n", test_output)

    # -----------------------------
    # STEP 5 — FIX LOOP
    # -----------------------------
    retries = 2

    while retries > 0:

        if not has_test_failures(test_output):
            break

        print(f"🔁 Retry {2 - retries + 1}")

        fixed_code = fix_code_with_llm(test_output, code)

        if (
            not fixed_code or
            len(fixed_code.strip()) < 50 or
            not is_valid_code(fixed_code)
        ):
            break

        code = fixed_code
        save_files(code, tests)

        new_output = run_tests()
        print("🧪 TEST OUTPUT:\n", new_output)

        if new_output == test_output:
            break

        test_output = new_output
        retries -= 1

    return {
        "plan": plan,
        "code": code,
        "tests": tests,
        "run_output": "skipped",
        "test_output": test_output
    }