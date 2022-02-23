#!/usr/bin/bash
echo $1
dd if="$1" of="/dev/shm/test"
