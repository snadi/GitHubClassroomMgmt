# Scripts to manage GitHub Classroom

This folder contains scripts to collect assignments or labs and push feedback to student repositories in a given GitHub organization. There are no repository creation scripts here, since we use GitHub classroom for this part.



## Dependencies

- Python 3
- [github3](https://github.com/sigmavirus24/github3.py)

````shell
# Quick installation steps
pip3 install -r requirements.txt
````

These scripts have been tested with Python 3.9.1(latest).



## Directory structure

```
.
├── ccids.txt                   # Contains ccids you need to grade
├── repo_names.txt              # Contains repo names you need to grade
├── collect_repos.py            # Collect repos
├── config                      # Configration file for collect_repos.py
├── push_feedback.sh            # Push feedback to all repos
├── README.md                   # This file
├── requirements.txt            # For dependencies installation
├── token_file.txt              # Your Github access token(You need to create this file)
├── update_repos.sh             # Update all repos
├── team_check.py               # Cross-check student teams
├── roster.csv                  # GitHub Classroom roster
├── pairs.csv                   # Assignment pairs list
│
├── assignment1                 # A subdirectory named with an assignment or lab name
│   │                           # It's automatically created after running collect_repos.py
│   ├── repo1
│   │   ├── feedback.md         # Feedback you made. Could have been generated
│   │   │                       # with marking scripts you had or added manually
│   │   └── ...
│   ├── repo2                   # Student's repository (e.g., labs-GithubUsername)
│   └── ...                
└── ...                         # Other subdirectories (e.g., labs, assignment2, etc.)
```



## Instructions

To use these scripts, please follow the following steps:

1. **Add SSH keys to your GitHub account**

   - Follow the steps on this website: https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

2. **Generate a personal access token**

   - Go to https://github.com/settings/tokens, click `Generate new token`, select all scopes and click `Generate token`.

   - Remember to copy the token and paste it to a file created by yourself named `token_file.txt`.

3. **Configure**

   - Open `config`, make your own configuration. Typically, you need to change `username`, `prefix` and `deadline`.
   - `prefix` is the name of lab or assignment you are grading (e.g., assignment1).
   - If you want to collect all repos, provide no value to key `list`. Otherwise, use `ccid_list.txt` as value.
   - If you want to collect repos with the latest commit, provide no value to key `deadline`. Otherwise, the script finds the closest commit that happens before a given deadline (inclusive) and clones/checks out the repository at that commit.

4. **(For labs) Add ccids**

   - Download GitHub Classroom roster to the root directory, rename it to `roster.csv`.
- Open `ccids.txt`, paste ccids you need to grade to this file.
   - All ccids are emails (e.g., zicun@ualberta.ca), one ccid per line.
   - Make sure set `repo_name_list =   ` (no value is supplied) in `config`. Otherwise, the script won't look at `ccids.txt`.

5. **(For assignments) Add repo names** 

   - Open `repo_names.txt`, paste repository names (team names in assignments) to this file, one name per line.
   - Open `config`, set `repo_name_list = repo_names.txt`.

6. **Collect repositories**

   ```shell
   # Run this command in the root directory.
   
   python3 collect_repos.py
   
   # If you are grading assignment1,
   # a directory called 'assignment1' will be created,
   # where all the repos for assignment1 will be cloned to.
   
   # At the end, the script will output some error messages 
   # including any ccid it couldn't find in the student list.
   ```

7. **Grade**

   - Run whatever grading scripts you have or grade manually and create a feedback file in each repository.

8. **Push feedback to student's repository**

   ```shell
   # If your feedback is in 'feedback.md', run this command in the root directory.
   
   ./push_feedback.sh feedback.md
   
   # This will go through all repos in the subdirectories (check directory structure above),
   # push every file named 'feedback.md' to corresponding repositories,
   # so to name all feedback files with the same name is a good move.
   
   # Because the collection process leaves the repository in a detached state,
   # this script will checkout main branch, pull with rebase, and push.
   ```

9. **Update repositories (optional)**

   - Because all labs of one student are in one repository, every time when you start grading a new lab, you need to assign a new value to `deadline` and run `python3 collect_repos.py`.
   - All repositories will be updated to the closest commit before the new deadline.

10. **Cross-check student teams (optional)**

   - Download assignment pairs list to the root directory, rename it to `pairs.csv`.

     ```shell
     # Run this command in the root directory
     
     python3 team_check.py
     
     # For each student in the pairs.csv
     # This script will check if they join the correct team on GitHub
     
     # It will also check if the team information in roster.csv is correct
     ```

   - The results will be printed out in the terminal and be saved to two files:

     - `problematic_students.csv`: compares the `pairs.csv` to the actual team memberships from the GitHub organization.
     - `problematic_students_roster.csv`: compares the `pairs.csv` to the `roster.csv`.

   - Sample `problematic_students.csv` (empty cell means student joined no team):

     | CCID            | GitHub username | expected team | current team  |
     | --------------- | --------------- | ------------- | ------------- |
     | xxx@ualberta.ca | xxx             | Asgmt1_Team1  | Asgmt1_Team2  |
     | xxx@ualberta.ca | xxx             | Asgmt1_Team3  |               |
     | xxx@ualberta.ca | xxx             | Asgmt1_Team5  | Asgmt1_Team10 |

   - Sample `problematic_students_roster.csv`:

     | CCID            | GitHub username | expected team | team in roster |
     | --------------- | --------------- | ------------- | -------------- |
     | xxx@ualberta.ca | xxx             | Asgmt1_Team1  |                |
     | xxx@ualberta.ca | xxx             | Asgmt1_Team3  |                |
     | xxx@ualberta.ca | xxx             |               | Asgmt1_Team10  |

     

## Troubleshooting

1. **github3.py installation issuses**
  
   As described above, you need to install github3.py in order to use the scripts, and if it's your first time using the GitHub module on the lab machines, you may encounter the below errors when trying to install the github3 module:
   
   ```
   Command "/usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-
   89vz819b/cryptography/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).
   read().replace('\r\n', '\n'), __file__, 'exec'))" install --record /tmp/pip-197ans87-record/
   install-record.txt --single-version-externally-managed --compile --user --prefix=" failed 
   with error code 1 in /tmp/pip-build-89vz819b/cryptography/
   ```

   or

   ```
   Failed buidling wheel for cryptography
   ```

   Running the command below fixes the above errors, and then you'll be able to run the installation as descibed under `Quick Installation Steps`:

   ```
   pip3 install --upgrade pip setuptools wheel
   ```

2. **ccid_list.txt and student_list.csv file issues**

   If your `ccid_list.txt` or `student_list.csv` files are improperly formatted, the scripts may run into a `KeyError` in execution. Make sure there isn't a trailing newline at the bottom of the file; you may need to open the `student_list.csv` file in a text editor rather than spreadsheet software to correct the formatting.
