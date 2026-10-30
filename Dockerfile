FROM python:3.11-slim

WORKDIR /app

COPY ims.py .
COPY products.json .

CMD ["python", "ims.py"]