#!/bin/bash

set -e
set -u

ZFS_INST="$( which zpool > /dev/null 2>&1 || echo not-installed )"
if [ "$ZFS_INST" == "not-installed" ]; then
	echo "ZFS is not installed."
	exit 1
fi 

zpool status -v
echo
zpool list -v
echo
zfs list
echo
zpool iostat -vl
