FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y socat libseccomp-dev libc-bin gdb && \ 
    rm -rf /var/lib/apt/lists/*

RUN useradd notes 
WORKDIR /home/notes/

COPY ./challenge/flag.txt .
COPY ./challenge/new_chall . 
COPY ./challenge/libc.so.6 . 
COPY ./challenge/ld-linux-x86-64.so.2 .
COPY ./challenge/entrypoint.sh .

RUN chmod +x entrypoint.sh new_chall libc.so.6 ld-linux-x86-64.so.2 && chown -R notes:notes . 
RUN ls -l && pwd && ldd new_chall
EXPOSE 9005
USER notes 

CMD ["./entrypoint.sh"]

