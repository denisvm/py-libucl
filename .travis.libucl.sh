#!/bin/sh
set -e

LIBUCL_DEFAULT_REPO=git://github.com/vstakhov/libucl
LIBUCL_DEFAULT_BRANCH=master

LIBUCL_REPO=${LIBUCL_REPO:-$LIBUCL_DEFAULT_REPO}
LIBUCL_BRANCH=${LIBUCL_BRANCH:-$LIBUCL_DEFAULT_BRANCH}

git clone --depth=1 -b "$LIBUCL_BRANCH" "$LIBUCL_REPO" vendor/libucl
cd vendor/libucl
./autogen.sh
./configure --enable-urls
make all
sudo make install
sudo ldconfig
