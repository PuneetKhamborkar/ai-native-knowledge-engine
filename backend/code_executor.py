import os
import subprocess

BASE_DIR = "generated_code"


def save_files(code, tests):
    os.makedirs(BASE_DIR, exist_ok=True)

    app_path = os.path.join(BASE_DIR, "app.py")
    test_path = os.path.join(BASE_DIR, "test_app.py")

    with open(app_path, "w") as f:
        f.write(code)

    with open(test_path, "w") as f:
        f.write(tests)

    return app_path


def run_app(file_path):
    try:
        result = subprocess.run(
            ["python3", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)


def run_tests():
    try:
        result = subprocess.run(
            ["python3", "-m", "pytest", "generated_code"],
            capture_output=True,
            text=True
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)