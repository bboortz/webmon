#!/bin/bash

set -u
set -e

FNAME=$( readlink -f $0 )
DNAME=${FNAME%/*}

source ${DNAME}/.venv/bin/activate
${DNAME}/gather.py
${DNAME}/render.py
