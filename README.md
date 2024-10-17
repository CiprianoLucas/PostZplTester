# Programa para testar recebimento de ZPL via POST

### Windows
```bash
py -m venv venv
venv/Scripts/activate
pip install fastapi httpx uvicorn
uvicorn main:app --reload --port 4000
```

### Linux
```bash
python3 -m venv venv
source venv/Scripts/activate
pip install fastapi httpx uvicorn
uvicorn main:app --reload --port 4000
```

#### http://127.0.0.1:4000/send_string/

Os arquivos serão salvos na pasta "ZPLs", O nome do arquivo será o código de rastreio.