FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаем фейковую папку с документами
RUN mkdir -p /app/documents/
RUN echo "Hello, world!" > /app/documents/hello.txt

COPY main.py .

# Запускаем сервер
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]