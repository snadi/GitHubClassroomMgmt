'''
This script collects all student repositories for a given assignment in a given organization at a given deadline
Run this script from inside a directory that contains/will contain all the repos for this assignment
'''

from github3 import login
import getpass
import subprocess
import csv
import argparse
import os

def run(username, tokenFile, organization, deadline,assignment):
	with open(tokenFile, 'r') as file:
			token = file.readline().strip()
	github = login(username,token=token)
	memberships = github.organization_memberships()
	course = None

	for membership in memberships:
		if membership.organization.login.lower() == organization.lower():
			course = membership.organization
			break

	currentDir = os.getcwd()

	for repo in course.repositories():
		if(repo.name.startswith(assignment)):
			if (os.path.exists(repo.name)): #check first that we don't already have a local copy of this repo
				os.chdir(currentDir + "/" + repo.name)
				subprocess.call("git pull", shell=True)
				subprocess.call("git checkout \"`git rev-list master -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);
				os.chdir(currentDir)
			else:
				subprocess.call("git clone " + repo.ssh_url, shell=True)
				os.chdir(currentDir + "/" + repo.name)
				subprocess.call("git checkout \"`git rev-list master -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);
				os.chdir(currentDir)


parser = argparse.ArgumentParser(description='Collect repos')
parser.add_argument('--username', help='Github username')
parser.add_argument('--tokenFile', help='File containing your github token')
parser.add_argument('--deadline', help="Deadline of the given assignment in format \"YYYY-MM-DD HH:MM:SS -0700\" where -0700 indicates the MST time zone")
parser.add_argument('--organization', help="Course github organization")
parser.add_argument('--assignment', help="Assignment name")

args = parser.parse_args()
run(username=args.username, tokenFile=args.tokenFile, organization=args.organization, deadline=args.deadline, assignment=args.assignment)
