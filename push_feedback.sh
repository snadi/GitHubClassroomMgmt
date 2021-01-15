#!/bin/bash

#IMPORTANT: This script will checkout master first which will override any changes to already tracked files

feedback_filename=$1

for dir in */; do
    cd $dir
    for subdir in */; do
        if [[ -d $subdir ]]; then
            echo "Pushing for $subdir"
            cd $subdir
            git checkout main
            git add $1
            git commit $1 -m "Grade assignment"
            git pull --rebase
            git push
            cd ..
        fi
    done
    cd ..
done
