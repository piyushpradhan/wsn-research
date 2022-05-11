#!/bin/bash

# Add the full path processes to run to the array
PROCESSES_TO_RUN=("/home/mediocre/projects/wsn-research/optimize.py" \
                  "/home/mediocre/projects/wsn-research/optimize.py")
# You can keep adding processes to the array...

for i in ${PROCESSES_TO_RUN[@]}; do
    ${i%/*}/./${i##*/} > ${i}.log 2>&1 &
    # ${i%/*} -> Get folder name until the /
    # ${i##*/} -> Get the filename after the /
done

# Wait for the processes to finish
wait
