#!/bin/sh

EXEC="./new_chall"
PORT=9005

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr