FROM python:3.12

WORKDIR /app

COPY apigateway/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "run.py"]
