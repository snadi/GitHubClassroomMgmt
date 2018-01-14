#!/bin/bash

#I have my students submit a file called <ccid>.txt that contains their github id on eClass, such that I can maintain
#a mapping from their github id to their CCID.
#Assuming you went to the eClass assignment and did "Download all submissions" and unarchived the file, you will be
#in a folder that contains several folders, one for each student in the class. Inside that folder, will be the <ccid>.txt
#file you are after. Running this script processes the txt file in each folder and outputs a csv mapping with two
#columns CCID and github id.

csv_file="ccid_to_github_mapping.csv"
echo "CCID,GITHUB_ID" > $csv_file

for dir in ./* ; do
  if [ -d "$dir" ]; then
 	#there should be just one file in there so this loop will run once
  for fullfile in "$dir"/*.txt; do

	#https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash
	filename=$(basename "$fullfile")
	ccid="${filename%.*}"

	githubID=`cat "$fullfile"`
	echo "$ccid,$githubID" >> $csv_file
	
	done
  fi
done