# Use an official Python runtime as the base image
FROM python:3.9-slim

WORKDIR /app
RUN adduser --disabled-password --force-badname alphaCTF
RUN pip install gunicorn flask
COPY challenge .
USER alphaCTF
EXPOSE 1402

# Run the app
CMD ["gunicorn", "--bind=0.0.0.0:1402", "--workers=3", "app:app"]
