#!/bin/sh

EXEC="./chall_patched"
PORT=9006

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr