repoName=$1

git clone https://github.com/CMPUT201-W17/$repoName

cd $repoName

mkdir Labs
mkdir Assignments
echo "#Labs directory">>Labs/README.md
echo "#Assignments directory">>Assignments/README.md

git add Assignments/*
git add Labs/*
git commit Assignments/ Labs/ -m "Add Labs and assignments directories"

git push