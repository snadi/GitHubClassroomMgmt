# Private GitHub repos 

This folder has scripts that create private GitHub repos in an existing organization. Each repo will then have the same directory structure. Scripts still need some cleanup and moving some things as parameters but they should work for now :-) I use python for creating the repos.

- Make sure you have the python library github3 installed (https://github.com/sigmavirus24/github3.py)
- run `python create_student_repos.py`. The script reads the StudentList.csv file and creates a private repo with each student's name and adds them as collaborator on the repo. The python script then runs the shell script CreateRepoStructure.sh to checkout out each repo and create the appropriate director structure in it. The directory structure is in the DirNames file so change it as needed.
