FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \ 
    gcc \
    python3-dev \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python3", "main.py"]
