#!/bin/bash

set -u
set -e

FNAME=$( readlink -f $0 )
DNAME=${FNAME%/*}

date

source ${DNAME}/.venv/bin/activate
python3 ${DNAME}/gather.py
python3 ${DNAME}/render.py
