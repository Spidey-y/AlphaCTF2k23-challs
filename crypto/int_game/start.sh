#!/bin/sh
USER="chall"
EXEC="./server.py"
PORT=1299
socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive,su="$USER" exec:"$EXEC",stderr
