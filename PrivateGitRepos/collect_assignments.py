'''
This script collects all student repositories in the organization at a given deadline
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
		print repo, repo.name
		subprocess.call("git clone " + repo.clone_url, shell=True)
		os.chdir(currentDir + "/" + repo.name)
		#subprocess.call("cd " + repo.name, shell=True)
		print("changed to " + os.getcwd())
		subprocess.call("git checkout \"`git rev-list master -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);
		#subprocess.call("cd ..", shell=True)
		os.chdir(currentDir)
		print(" back to" + os.getcwd())


parser = argparse.ArgumentParser(description='Collect repos')
parser.add_argument('--username', help='Github username')
parser.add_argument('--token', help='Github token file')
parser.add_argument('--deadline', help="Deadline of the given assignment in format \"%Y-%m-%d %H:%M:%S -700\"")
parser.add_argument('--organization', help="Course organization")

args = parser.parse_args()
run(args.username, args.token, args.organization,args.deadline)
