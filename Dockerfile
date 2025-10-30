FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HF_TOKEN=${HF_TOKEN}

EXPOSE 5000

CMD ["python", "backend/app.py"]
