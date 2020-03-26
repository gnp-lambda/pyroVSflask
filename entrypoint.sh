#!/bin/sh

# Uso: entrypoint.sh [flask/pyro] payload1 [payload2] ... [payloadN]
TYPE=$1
shift

set -x

for size in "$@"; do
    python -m timeit -n 1000 -s "from ${TYPE}_client import main" "main($size)"
done
