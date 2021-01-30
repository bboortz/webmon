#!/bin/bash

set -u
set -e

FNAME=$( readlink -f $0 )
DNAME=${FNAME%/*}
DNAME=${DNAME%/*}

date

if [ ! -d "${DNAME}/.venv" ]; then
    python -m venv ${DNAME}/.venv
fi
source ${DNAME}/.venv/bin/activate
pip install -U -r requirements.txt pip
