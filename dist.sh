#!/bin/sh

set -e

poetry run pyinstaller \
  --name mon-appli \
  --onefile \
  --paths . \
  --add-data "src/data:src/data" \
  src/hello.py