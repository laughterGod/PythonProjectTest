#!/bin/bash

#exe_path=`cd $(dirname $0);pwd` 1>&2 && \
#export PATH="$exe_path/python2/bin:$PATH" 1>&2 && \
#export LD_LIBRARY_PATH="$exe_path/python2/lib:$LD_LIBRARY_PATH" 1>&2 && \

#run main.py
python ./bin/main.py 2>err
