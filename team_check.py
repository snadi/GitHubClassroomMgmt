import pandas as pd
from github3 import login
import configparser
import numpy as np


### Get team members
config = configparser.ConfigParser()
config.read('config')
config = config['DEFAULT']

username = config['username']
token = config['token']
organization = config['organization']
pairs = config['pairs']
roster = config['roster']

with open(token, 'r') as f:
    token = f.readline().strip()
    
github = login(username,token=token)
memberships = github.organization_memberships()
course = None

for membership in memberships:
    if membership.organization.login.lower() == organization.lower():
        course = membership.organization
        break
    
teams = {team.name : team for team in list(course.teams())}
tas = teams['TAs'].members()
instructors = teams['Instructors'].members()
print("Getting team members, please wait...")
team_members = {team.name: [m.login for m in set(team.members()) - \
    set(tas) - set(instructors)] for team in teams.values()}


### Preprocess
pairs_df = pd.read_csv(pairs)
roster_df = pd.read_csv(roster)

header = ['CCID', 'GitHub username', 'expected team', 'current team']
pairs_df = pairs_df[['Email', 'Assignment 1 Team']]
pairs_df.columns = ['CCID', 'expected team']
pairs_df = pairs_df.reindex(columns = header)

roster_df = roster_df[['github_username', 'identifier', 'group_name']]
roster_df.columns = ['GitHub username', 'CCID', 'expected team']


### Check student teams
pairs_result = pairs_df.copy()
pairs_result['GitHub username'] = pd.merge(pairs_df, roster_df, on='CCID')['GitHub username_y']

pairs_result['current team'] = pairs_result['GitHub username'].apply(lambda x: \
    [k for k,v in team_members.items() if x in v]).apply(lambda x: len(x) \
        and (len(x) == 1 and x[0] or str(x)) or np.nan)

pairs_result = pairs_result.replace(np.nan, '')
pairs_result = pairs_result.loc[pairs_result['expected team'] != \
    pairs_result['current team']].reset_index(drop=True)

print('\n-----\nProblematic students\n-----\n')
print(pairs_result)
pairs_result.to_csv('problematic_students.csv', index=False)


### Check roster
roster_result = pd.merge(pairs_df, roster_df, on='CCID', how='outer')
roster_result = roster_result[['CCID', 'GitHub username_y', 'expected team_x', 'expected team_y']]
roster_result.columns = header[:3] + ['team in roster']
roster_result = roster_result.replace(np.nan, '')
roster_result = roster_result.loc[roster_result['expected team'] != \
    roster_result['team in roster']].reset_index(drop=True)

print('\n-----\nRoster\n-----\n')
print(roster_result)
roster_result.to_csv('problematic_students_roster.csv', index=False)