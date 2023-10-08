#!/bin/sh

while true; do
  d=$(date)

  printf "\033[34m$d\n\033[33m$d\n\033[32m$d\n\033[0m"

  sleep 0.5
  tput cuu 3
  tput ed
done

