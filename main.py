from fastapi import FastAPI
from pydantic import BaseModel
import base64
import os
from io import BytesIO

app = FastAPI()

class SendStringRequest(BaseModel):
    content: str
    tracking: str
    responseType: str
    fileType: str

@app.post("/send_string/")
async def send_string(request: SendStringRequest):
    file = request.content
    tracking_code = request.tracking
    response_type = request.responseType
    file_type = request.fileType

    file_bytes = file.encode()
    if response_type == 'base64':
        file_bytes = base64.b64decode(file_bytes)

    directory = os.path.join(os.path.dirname(__file__), 'ZPLs')

    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{tracking_code}.{file_type}")

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    return {"message": "Arquivo salvo com sucesso", "file_path": file_path}
