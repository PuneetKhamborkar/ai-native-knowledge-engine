import yaml
import os

BASE_PATH = "../kdf/auto"

os.makedirs(BASE_PATH, exist_ok=True)

def save_kdf(kdf):

    file_path = os.path.join(BASE_PATH, f"{kdf['id']}.yaml")

    with open(file_path, "w") as f:
        yaml.dump(kdf, f)

    return file_path