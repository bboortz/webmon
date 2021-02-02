#!/bin/bash

set -u
set -e

FNAME=$( readlink -f $0 )
DNAME=${FNAME%/*}

date

pidof bash

source ${DNAME}/.venv/bin/activate
python3 ${DNAME}/webmon.py
