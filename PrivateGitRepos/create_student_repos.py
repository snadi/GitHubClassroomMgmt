'''
This script reads a csv file that includes student names and their GitHub accounts
For each student, it creates the GitHub repo, creates the directory structure, and pushes all changes.
'''
from github3 import login
import getpass
import subprocess
import csv

def get_name(repository):
	return repository.name

def run():
	github = login('snadi', password = getpass.getpass())
	memberships = github.organization_memberships()
	seminar = None

	for membership in memberships:
		if membership.organization.login == "spl-sem":
			seminar = membership.organization
			break

	existing_repos = set(map(get_name,seminar.repositories()))	

	with open("StudentList.csv") as studentFile:
		reader = csv.DictReader(studentFile)
		for student in reader:
			repoName = "".join(student['Name'].split())
			if not repoName in existing_repos and len(student['GitHubUsername']) > 0:
				repository = seminar.create_repository(repoName, private=True)
				repository.add_collaborator(student['GitHubUsername'])
				subprocess.call("./CreateRepoStructure.sh " + repoName, shell=True)

run()