#!/bin/sh
set -e

: ${LIBUCL_REPO="git://github.com/vstakhov/libucl"}
: ${LIBUCL_BRANCH="master"}

git clone --depth=1 -b "$LIBUCL_BRANCH" "$LIBUCL_REPO" vendor/libucl
cd vendor/libucl
./autogen.sh
./configure --enable-urls
make all
sudo make install
sudo ldconfig
