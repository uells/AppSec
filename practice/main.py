from fastapi import FastAPI, HTTPException, Request
import os
import httpx

app = FastAPI()

# --- СЕКРЕТНАЯ ЗОНА ---
# Этот эндпоинт имитирует внутренний микросервис, который не торчит в интернет.
@app.get("/internal/secret")
async def get_secret(request: Request):
    # Проверяем, что запрос пришел с самого сервера, а не снаружи
    if request.client.host != "127.0.0.1":
         raise HTTPException(status_code=403, detail="Direct access denied! Only localhost allowed.")
    return {"flag": "FLAG{SSRF_MASTER_BYPASS}"}


# --- УЯЗВИМОСТЬ 1: LFI (Просмотр документов) ---
@app.get("/api/preview")
async def preview_document(doc_path: str):
    """
    Эндпоинт для чтения текстовых документов. 
    Разработчик поставил "надежный" фильтр от Path Traversal.
    """
    if "../" in doc_path:
        raise HTTPException(status_code=403, detail="Hack detected! '../' is forbidden.")
    
    base_directory = "/app/documents/"
    target_file = os.path.join(base_directory, doc_path)
    
    try:
        with open(target_file, "r") as f:
            content = f.read()
        return {"document": target_file, "content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except IsADirectoryError:
        raise HTTPException(status_code=400, detail="That is a directory, not a file")


# --- УЯЗВИМОСТЬ 2: SSRF (Загрузчик по URL) ---
@app.get("/api/fetch")
async def fetch_url(url: str):
    """
    Эндпоинт скачивает данные по переданной ссылке.
    Разработчик попытался запретить обращение к внутренним сервисам.
    """
    blacklist = ["localhost", "127.0.0.1", "0.0.0.0"]
    for bad_word in blacklist:
        if bad_word in url:
            raise HTTPException(status_code=403, detail="Access to internal network is strictly forbidden!")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
        return {"status": response.status_code, "body": response.text}
    except Exception as e:
        return {"error": str(e)}