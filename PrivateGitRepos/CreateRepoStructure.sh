#!/bin/bash

repoName=$1

git clone https://github.com/CMPUT201-W17/$repoName

cd $repoName

cp ../UALBERTA-CMPUT201License/CMPUT201License.md LICENSE.md

git add LICSENSE.md
git commit -am "Add license file"

#Lab folders
mkdir Labs
echo "#Labs directory\n Please do not change this directory structure. Each lab should go under its respective folder.">>Labs/README.md
for labNum in 1 2 3 .. 12
do
	mkdir Labs/Lab$labNum
done

#Assignment folders
mkdir Assignments
echo "#Assignments directory\n Please do not change this directory structure. Each assignment should go under its respective folder.">>Assignments/README.md
for labNum in 1 2 3
do
	mkdir Assignments/Assignment$labNum
done

git add --all
git commit -am "Add Labs and assignments directories"

git push
