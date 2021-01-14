'''
This script collects the current state of all student repositories for a given assignment in a given organization 
Run this script from inside a directory that contains/will contain all the repos for this assignment
'''

from github3 import login
import getpass
import subprocess
import csv
import configparser
import os

def get_repo(repo, dir):
	repoDir = os.path.join(dir, repo.name)
	if (os.path.exists(repoDir)): #check first that we don't already have a local copy of this repo
		os.chdir(repoDir)
		subprocess.call('git pull', shell=True)
		if deadline:
			subprocess.call("git checkout \"`git rev-list --all -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);
	else:
		os.chdir(dir)
		subprocess.call('git clone ' + repo.ssh_url, shell=True)
		if deadline:
			os.chdir(repoDir)
			subprocess.call("git checkout \"`git rev-list --all -n 1 --first-parent --before=\"" + deadline + "\"`\"", shell=True);

def run(username, token, organization, prefix, list, deadline):
	with open(token, 'r') as f:
		token = f.readline().strip()

	github = login(username,token=token)
	memberships = github.organization_memberships()
	course = None

	for membership in memberships:
		if membership.organization.login.lower() == organization.lower():
			course = membership.organization
			break

	newDir = os.getcwd() + "/{}".format(prefix) #pull all repos to this folder
	if not os.path.exists(newDir):
		os.mkdir(newDir)

	with open('student_list.csv', mode='r') as f:
		reader = csv.reader(f)
		mapping = {rows[1]:rows[2] for rows in reader}

	if list:
		with open(list, 'r') as f:
			ccids = [ccid.strip() for ccid in f.readlines()]
			gh_usernames = [mapping[ccid] for ccid in ccids]  #convert ccid to github username
	else:
		gh_usernames = []

	for repo in course.repositories():
		if len(gh_usernames):
			if repo.name.replace('{}-'.format(prefix), '') in gh_usernames:
				get_repo(repo, newDir)
		elif repo.name.startswith(prefix):
			get_repo(repo, newDir)

if __name__ == '__main__':
	config = configparser.ConfigParser()
	config.read('config')
	config = config['DEFAULT']
	
	username = config['username']
	token = config['token']
	organization = config['organization']
	prefix = config['prefix']
	list = config['list'] and config['list'] or None
	deadline = config['deadline'] and config['deadline'] or None
	
	run(username, token, organization, prefix, list, deadline)