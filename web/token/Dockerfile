FROM python:3.8.10-alpine

RUN pip install fastapi uvicorn pyjwt 
RUN adduser -D alphaCTF 
COPY ./challenge /home/alphaCTF/app 

USER alphaCTF 
WORKDIR /home/alphaCTF/app 
EXPOSE 5000
CMD ["python", "main.py"]