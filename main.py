from fastapi import FastAPI
from pydantic import BaseModel
import base64
import os

app = FastAPI()

class SendStringRequest(BaseModel):
    zpl: str
    codigoRastreamento: str

@app.post("/send_string/")
async def send_string(request: SendStringRequest):
    
    string = request.zpl
    tracking_code = request.codigoRastreamento

    base64_bytes = string.encode('utf-8')
    string_bytes = base64.b64decode(base64_bytes)
    decoded_string = string_bytes.decode('utf-8')
    
    directory = os.path.join(os.path.dirname(__file__), 'ZPLs')
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    file_path = os.path.join(directory, f"{tracking_code}.txt")
            
    with open(file_path, "w") as file:
        file.write(decoded_string)

    return {"message": "Arquivo criado com sucesso"}
