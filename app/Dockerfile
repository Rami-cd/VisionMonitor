FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir \
    --default-timeout=100 \
    --retries 10 \
    -r requirements.txt

COPY app/ .
COPY tracker_system/ ./tracker_system/
COPY config/ ./config/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]