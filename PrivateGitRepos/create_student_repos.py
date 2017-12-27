'''
This script reads a csv file that includes student names and their GitHub accounts
For each student, it creates the GitHub repo, creates the directory structure, and pushes all changes.
'''
from github3 import login
import getpass
import subprocess
import csv
import argparse

def get_name(repository):
	return repository.name

def get_repo(course, repository_name):
	for repo in course.repositories():
		if get_name(repo) == repository_name:
			return repo

def run(username, organization, tokenFile, studentList):

	with open(tokenFile, 'r') as file:
			token = file.readline().strip()
	github = login('snadi',token=token)
	memberships = github.organization_memberships()
	course = None

	for membership in memberships:
		if membership.organization.login.lower() == organization.lower():
			course = membership.organization
			break

	existing_repo_names = set(map(get_name,course.repositories()))	

	with open(studentList) as studentFile:
		#get licsense file
		subprocess.call("./getLicenseRepo.sh", shell=True)
		reader = csv.DictReader(studentFile)
		for student in reader:
			repoName = student['CCID'] + "-201-W18" 
			print "Reading ", repoName
			if not repoName in existing_repo_names and len(student['GitHubUsername']) > 0:
				print "Creating repository for ",repoName
				repository = course.create_repository(repoName, private=True)
				repository.add_collaborator(student['GitHubUsername'])
				subprocess.call("./CreateRepoStructure.sh " + organization + repoName, shell=True)

parser = argparse.ArgumentParser(description='Create repos')
parser.add_argument('--list', help='CSV file')
parser.add_argument('--token', help='Github token file')
parser.add_argument('--organization', help="Course github organization")
parser.add_argument('--username', help='Github username')

args = parser.parse_args()
run(args.username, args.organization, args.token, args.list)