#!/bin/sh

set -e

poetry run pyinstaller \
  --name mon-appli \
  --onefile \
  --paths . \
  src/hello.py