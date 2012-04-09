#!/usr/bin/python
#returns the value of the word passed in 
def wordValue(name):
	count = 0
	for letter in name.lower():
		count += ord(letter) - 96
	return count

#list of names
names = []
#total namescore count
nameCount = 0

#input file
inputFile = open('22.txt')

line = inputFile.readline()
#get the names from the file	
names = line.strip()[1:len(line)-2].split('","')

#sort the names
names.sort()

#go through names and add the name score
for i in range(len(names)):
	nameCount += ((i+1) * wordValue(names[i]))

print nameCount


