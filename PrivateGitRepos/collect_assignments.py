'''
This script collects all student repositories in a given organization at a given deadline
'''

from github3 import login
import getpass
import subprocess
import csv
import argparse
import os

def run(username, tokenFile, organization, deadline):
	with open(tokenFile, 'r') as file:
			token = file.readline().strip()
	github = login(username,token=token)
	memberships = github.organization_memberships()
	course = None

	for membership in memberships:
		print membership
		if membership.organization.login.lower() == organization.lower():
			course = membership.organization
			break

	currentDir = os.getcwd()

	for repo in course.repositories():
		print("Cloning" + repo)
		subprocess.call("git clone " + repo.clone_url, shell=True)
		os.chdir(currentDir + "/" + repo.name)
		subprocess.call("git checkout \"`git rev-list master -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);
		os.chdir(currentDir)


parser = argparse.ArgumentParser(description='Collect repos')
parser.add_argument('--username', help='Github username')
parser.add_argument('--token', help='Github token file')
parser.add_argument('--deadline', help="Deadline of the given assignment in format \"%Y-%m-%d %H:%M:%S -0700\" where -0700 indicates the MST time zone")
parser.add_argument('--organization', help="Course github organization")

args = parser.parse_args()
run(args.username, args.token, args.organization,args.deadline)
