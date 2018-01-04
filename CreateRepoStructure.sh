#!/bin/bash

organization=$1
repoName=$2

repoURL="git@github.com:$organization/$repoName.git"
git clone $repoURL

cd $repoName

cp ../UALBERTA-CMPUT201License/CMPUT201License.md LICENSE.md

git add LICENSE.md
git commit -am "Add license file"

#Lab folders
mkdir Labs
echo "# Labs directory <br/><br/> Please do not change this directory structure. Each lab should go under its respective folder.">>Labs/README.md
git add Labs/README.md
for labNum in {1..12}
do
    mkdir Labs/Lab$labNum
    echo "# Lab $labNum">> Labs/Lab$labNum/README.md
    echo "<br/>You should replace this ReadMe with your own as needed according to the lab instructions">> Labs/Lab$labNum/README.md
    git add Labs/Lab$labNum/README.md
done

#Assignment folders
mkdir Assignments
echo "# Assignments directory <br/><br/> Please do not change this directory structure. Each assignment should go under its respective folder.">>Assignments/README.md
git add Assignments/README.md
for assignmentNum in {1..3};
do
    mkdir Assignments/Assignment$assignmentNum
    echo "# Assignment $labNum" >> Assignments/Assignment$assignmentNum/README.md
    echo "<br/>You should replace this ReadMe with your own according to the assignment instructions">> Assignments/Assignment$assignmentNum/README.md
    git add Assignments/Assignment$assignmentNum/README.md
done

git commit -am "Add Labs and assignments directories"

git push
