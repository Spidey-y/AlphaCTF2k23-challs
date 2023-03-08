FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --force-badname alphaCTF
USER alphaCTF
EXPOSE 8080

CMD exec gunicorn --bind :8080 --workers 4 --threads 4 --timeout 0 app
