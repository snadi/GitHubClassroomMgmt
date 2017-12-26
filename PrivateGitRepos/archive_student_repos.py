'''
This script reads a csv file that includes student names and their GitHub accounts
For each student, it archives the respective repo
'''
from github3 import login
import getpass
import subprocess
import csv
import argparse

def get_name(repository):
	return repository.name

def run(user, tokenFile, org, suffix=""):
	with open(tokenFile, 'r') as file:
			token = file.readline().strip()
	github = login(user,token=token)
	memberships = github.organization_memberships()
	course = None

	for membership in memberships:
		if membership.organization.login.lower() == org.lower():
			course = membership.organization
			break

	existing_repo_names = set(map(get_name,course.repositories()))	

	for repoName in existing_repo_names:
		if(repoName.endswith("-201")):
			new_name = repoName + "-" + suffix
			print "Archiving " + repoName + " as " + new_name
			#stupid way to do this.. find a proper API but temp for now
			command = "curl \
	-H \"Authorization: token " + token +"\" \
	-X PATCH \
	--data '{ \"archived\": true, \"name\": \"" + new_name + "\"}' \
	https://api.github.com/repos/" + org + "/" + repoName
			subprocess.call(command, shell=True)

parser = argparse.ArgumentParser(description='Create repos')
parser.add_argument('--token', help='Github token file')
parser.add_argument('--suffix', help='Optional suffix to add to repo name when archiving')
parser.add_argument('--org', help='Organization name')
parser.add_argument('--user', help='GitHub username')

args = parser.parse_args()
run(args.user, args.token, args.org, args.suffix)
