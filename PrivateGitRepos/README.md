# Private GitHub repos 

This folder has scripts that create private GitHub repos in an existing organization. Each repo will then have the same directory structure. Scripts still need some cleanup and moving some things as parameters but they should work for now :-) I use python for creating the repos.

Make sure you have the python library github3 installed (https://github.com/sigmavirus24/github3.py)

Script descriptions:

- `create_student_repos.py`: The script reads the StudentList.csv file and creates a private repo with each student's name and adds them as collaborator on the repo. The python script then runs the shell script CreateRepoStructure.sh to checkout out each repo and create the appropriate directorY structure in it
- `archive_student_repos.py`: archives all existing repos in the organization. Probably could use a few more filters to see what you want to archive. The github3 API does not have support for archiving yet so currently using a naive concatenated curl command to do the archiving
- `collect_assignments.py`: Finds the closes commit that happens before a given deadline (inclusive) and checks out the repository at that commit. 
