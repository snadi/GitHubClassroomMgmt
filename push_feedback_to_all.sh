#!/bin/bash

#IMPORTANT: This script will checkout master first which will override any changes to already tracked files

feedback_filename=$1

for dir in */; do
    if [[ -d $dir ]]; then
    	echo "Pushing for $dir"
       	cd $dir
        git checkout master
        git add $1
        git commit $1 -m "Grade assignment"
        git pull --rebase
        git push
        cd ..
    fi
done
