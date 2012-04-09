#!/usr/bin/python
from common import *

#get input file
inputFile = open('67.txt')

#set the root node (only purpose is to make it easy to print out)
root = treeNode(int(inputFile.readline().strip()))

#two lists to use
tmpArray = [root]
tmpArray2 = []

#Build the tree and by going through remaining lines in the file
for line in inputFile:
	#get the numbers for the line
	values = line.strip().split()
	#get the left now
	leftNode = treeNode(int(values[0]),tmpArray[0])
	
	#set the list as a new list
	tmpArray2 = [leftNode]
	#go through all the nodes and set their children
	for i in range(len(tmpArray)):
		rightNode = treeNode(int(values[i+1]), tmpArray[i])
		tmpArray[i].addLeftNode(leftNode)
		tmpArray[i].addRightNode(rightNode)
		leftNode = rightNode
		tmpArray2.append(leftNode)
	#copy the list
	tmpArray = list(tmpArray2)

#Start at leaf nodes. Then go up to their parents and choose the higher valued child and add their 
#value to the parent's value. Keep going through until we are at the root node
while(len(tmpArray2) > 1):
	#set the parent list as blank
	tmpArray = []
	
	#get the parent of the all the nodes. 
	for x in range(1, len(tmpArray2)):
		tmpArray.append(tmpArray2[x].parent)
		
	#for each parent find the higher valued child and add their total to the parents
	for parentNode in tmpArray:
		if parentNode.left.value > parentNode.right.value:
			parentNode.value += parentNode.left.value
		else:
			parentNode.value += parentNode.right.value

	#set the new children list as the current parent list	
	tmpArray2 = list(tmpArray)
	
#print the result
print root.value
