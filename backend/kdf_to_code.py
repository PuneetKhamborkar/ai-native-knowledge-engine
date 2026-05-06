def generate_code_from_kdf(kdf):

    endpoint = kdf["spec"]["endpoint"]
    method = kdf["spec"]["method"].lower()
    fields = kdf["spec"]["request"]["fields"]

    # Build request model fields
    field_lines = []
    for f in fields:
        line = f'{f["name"]}: str'
        if not f.get("required", True):
            line = f'{f["name"]}: Optional[str] = None'
        field_lines.append(line)

    fields_code = "\n    ".join(field_lines)

    code = f"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import uuid

app = FastAPI()

class RequestModel(BaseModel):
    {fields_code}


class ResponseModel(RequestModel):
    id: str


db: Dict[str, ResponseModel] = {{}}


@app.{method}("{endpoint}", status_code=201)
def create_item(item: RequestModel):
    item_id = str(uuid.uuid4())
    new_item = ResponseModel(id=item_id, **item.dict())
    db[item_id] = new_item
    return new_item
"""

    return code