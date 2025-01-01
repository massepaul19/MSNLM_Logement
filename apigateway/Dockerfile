FROM python:3.12

WORKDIR /app

COPY apigateway/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]




