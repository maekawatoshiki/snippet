#!/bin/sh -eux

VERSION=1.2.13

if [ "$(uname -m)" != "x86_64" -or "$(uname -s)" != "Linux" ]; then
  echo "This script only works on x86_64 Linux."
  exit 1
fi

wget https://github.com/aristocratos/btop/releases/download/v$VERSION/btop-x86_64-linux-musl.tbz
tar xvf btop-x86_64-linux-musl.tbz
(cd btop && ./install.sh)
rm -rf btop-x86_64-linux-musl.tbz btop
