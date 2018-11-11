#!/bin/bash

# Copyright 2015-2018 Vincent Jacques <vincent@vincent-jacques.net>

set -e

rm -f callgrind.out.*
valgrind --tool=callgrind python -m DrawTurksHead --width=3200 --height=2400 --leads=18 --bights=24 --radius-variation=1000 --line-width=20 --output=profiling/reference.png
mv callgrind.out.* /tmp/callgrind.out

kcachegrind /tmp/callgrind.out >/dev/null 2>&1 &
