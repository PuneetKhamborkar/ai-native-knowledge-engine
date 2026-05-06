from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Optional
import uuid

app = FastAPI()

# -----------------------------
# MODEL
# -----------------------------
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None


class Task(TaskCreate):
    id: str


# -----------------------------
# STORAGE
# -----------------------------
tasks: Dict[str, Task] = {}


# -----------------------------
# CREATE
# -----------------------------
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())

    new_task = Task(
        id=task_id,
        title=task.title,
        description=task.description
    )

    tasks[task_id] = new_task
    return new_task


# -----------------------------
# GET
# -----------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


# -----------------------------
# LIST
# -----------------------------
@app.get("/tasks")
def list_tasks():
    return list(tasks.values())


# -----------------------------
# UPDATE
# -----------------------------
@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = Task(
        id=task_id,
        title=task.title,
        description=task.description
    )

    tasks[task_id] = updated_task
    return updated_task


# -----------------------------
# DELETE
# -----------------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    return {"detail": "Task deleted"}