FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN addgroup ctf && adduser --ingroup ctf ctf

COPY challenge/ .

USER ctf

EXPOSE 1337

CMD ["socat","tcp-l:1337,reuseaddr,fork","EXEC:./auth"]