#!/bin/bash

#IMPORTANT: This script assumes that you have already done git checkout master after finishing your grading

feedback_filename=$1

for dir in */; do
    if [[ -d $dir ]]; then
    	echo "Pushing for $dir"
       	cd $dir
        git add $1
        git commit -am "Grade assignment"
        git pull --rebase
        git push
        cd ..
    fi
done