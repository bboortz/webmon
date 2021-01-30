#!/bin/bash

set -u
set -e

FNAME=$( readlink -f $0 )
DNAME=${FNAME%/*}

date

source ${DNAME}/.venv/bin/activate
${DNAME}/gather.py
${DNAME}/render.py
