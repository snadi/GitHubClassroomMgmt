#!/bin/bash

#IMPORTANT: This script will checkout master first which will override any changes to already tracked files

feedback_filename=$1
root=$PWD
find $root -iname $1 | sort -u | while read file; do
    repo_dir=$(dirname $file)
    if [ "$repo_dir" != "$root" ]; then
        echo "Pushing for $repo_dir"
        cd $repo_dir
        git checkout main
        git add $1
        git commit $1 -m "Grade assignment"
        git pull --rebase
        git push
    fi
done
