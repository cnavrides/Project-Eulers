#!/usr/bin/python

import os

currentDir = os.getcwd()

files = os.listdir(currentDir)

for f in files:
	try:
		num = f.split('.')[0]	
		tmp = int(num)
		os.system('mkdir ' + num)
		os.system('mv ' + num + '* ' + num)
		os.system('ln -s common.pyc ' + num+'/common.pyc')
	except:
		print f

	
