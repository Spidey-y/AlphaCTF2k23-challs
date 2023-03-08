FROM python:3.8-alpine

RUN apk --update add gcc build-base freetype-dev \
    libpng-dev openblas-dev \
    socat tcpdump 

RUN addgroup -S chall && adduser -S chall -G chall

RUN mkdir /chall 
WORKDIR /chall 

COPY ./flag.txt ./
COPY ./server.py ./ 
COPY ./start.sh ./


RUN chown -R root:chall /chall && \
    chmod 750 /chall && \
    chmod 444 /chall/flag.txt && \
    chmod 777 /chall/server.py && \
    chmod +x /chall/start.sh 



EXPOSE 1299



ENTRYPOINT ["./start.sh"]

