FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y socat patchelf libseccomp-dev libc-bin gdb && \ 
    rm -rf /var/lib/apt/lists/*

RUN useradd retwin 
WORKDIR /home/challenge/

COPY ./challenge/flag.txt . 
COPY ./challenge/chall_patched . 
COPY ./challenge/libc.so.6 . 
COPY ./challenge/ld-2.29.so . 
COPY ./challenge/entrypoint.sh . 

RUN chmod +x entrypoint.sh chall_patched libc.so.6 ld-2.29.so && chown -R retwin:retwin . 

EXPOSE 9006
USER retwin

CMD ["./entrypoint.sh"]