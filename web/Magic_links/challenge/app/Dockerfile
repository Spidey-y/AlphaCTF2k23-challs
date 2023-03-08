FROM python:3.9-slim-buster


WORKDIR /app
RUN chmod 777 /app
RUN adduser --disabled-password --force-badname alphaCTF

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
USER alphaCTF

CMD ["gunicorn", "--bind=0.0.0.0:5000", "--workers=3", "app:app"]