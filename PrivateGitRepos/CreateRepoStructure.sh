repoName=$1

git clone https://github.com/spl-sem/$repoName

cd $repoName

while read line; do
  mkdir $line
  echo "#Paper summary for $line">>$line/README.md
  git add $line/README.md
  git commit $line/README.md -m "Creating folder for $line"
done <../DirNames

mkdir Project
mkdir Project/Proposal
mkdir Project/Paper
mkdir Project/Presentation
echo "#Project directory">>Project/README.md
echo "#Paper directory">>Project/Paper/README.md
echo "#Presentation directory">>Project/Presentation/README.md
echo "#Proposal directory">>Project/Proposal/README.md

git add Project/*
git commit Project/ -m "project directory"

git push