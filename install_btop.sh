#!/bin/sh -eux

VERSION=1.2.13

wget https://github.com/aristocratos/btop/releases/download/v$VERSION/btop-x86_64-linux-musl.tbz
tar xvf btop-x86_64-linux-musl.tbz
(cd btop && ./install.sh)
rm -rf btop-x86_64-linux-musl.tbz btop
