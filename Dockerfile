FROM python:3.11-slim

WORKDIR /app

COPY ims.py .

CMD ["python", "ims.py"]