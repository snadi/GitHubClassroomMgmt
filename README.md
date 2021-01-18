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
├── ccid_list.txt               # Contains ccids you need to grade
├── collect_repos.py            # Collect repos
├── config                      # Configration file for collect_repos.py
├── push_feedback.sh            # Push feedback to all repos
├── README.md                   # This file
├── requirements.txt            # For dependencies installation
├── student_list.csv            # A mapping from ccids to github usernames
├── token_file.txt              # Your Github access token(You need to create this file)
├── update_repos.sh             # Update all repos
│
├── assignment1                 # A subdirectory named with an assignment or lab name 			│		│	
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

1. **Add SSH Keys to your GitHub Account**

   - Follow the steps on this website: https://www.inmotionhosting.com/support/server/ssh/how-to-add-ssh-keys-to-your-github-account

2. **Generate a personal access token**	

   - Go to https://github.com/settings/tokens, click `Generate new token`, select all scopes and click `Generate token`.

   - Remember to copy the token and paste it to a file created by yourself named `token_file.txt`.

3. **Configure**

   - Open `config`, make your own configuration. Typically, you need to change `username`, `prefix` and `deadline`.
   - `prefix` is the name of lab or assignment you are grading (e.g., assignment1).
   - If you want to collect all repos, provide no value to key `list`. Otherwise, use `ccid_list.txt` as value.
   - If you want to collect repos with the latest commit, provide no value to key `deadline`. Otherwise, the script finds the closest commit that happens before a given deadline (inclusive) and clones/checks out the repository at that commit. 

4. **Add ccids**

   - Open `ccid_list.txt`, paste ccids you need to grade to this file.
   - All ccids are emails (e.g., zicun@ualberta.ca), one ccid per line.

5. **Collect repositories**

   ```shell
   # Run this command in the root directory.
   
   python3 collect_repos.py
   
   # If you are grading assignment1, 
   # a directory called 'assignment1' will be created, 
   # where all the repos for assignment1 will be cloned to.
   ```

6. **Grade**

   - Run whatever grading scripts you have or grade manually and create a feedback file in each repository.

7. **Push feedback to student's repository**

   ```shell
   # If your feedback is in 'feedback.md', run this command in the root directory.
   
   ./push_feedback.sh feedback.md
   
   # This will go through all repos in the subdirectories (check directory structure above), 
   # push every file named 'feedback.md' to corresponding repositories, 
   # so to name all feedback files with the same name is a good move.
   
   # Because the collection process leaves the repository in a detached state, 
   # this script will checkout main branch, pull with rebase, and push.
   ```

8. **Update repositories (optional)**

   ```shell
   # Run this command in the root directory.
   
   ./update_repos.sh
   
   # This will go through all repos in the subdirectories and update them to the latest commit.
   ```

