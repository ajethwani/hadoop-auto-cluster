#! /usr/bin/python2

import os

f = open("/root/Desktop/Outputs/tasktrackers.txt","r");

for i in f.readlines():
	
	i=i.strip()
	
	###Copying to target PC
	b = os.system("sshpass -p 'redhat' scp /root/Desktop/tasktracker.py /root/Desktop/Outputs/jobtracker.txt root@"+str(i)+":/root/Desktop")
	
	if b == 0 :	
		print ("\n*****  COPIED TO "+i)
	
	###Running Config Script on target PC	
	a = os.system("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no -X root@"+str(i)+" \"python /root/Desktop/tasktracker.py\"")
	
	if a == 0 :	
		print("\n\n*****  "+i+" IS NOW A TASKTRACKER . . .")

raw_input("#####  CONFIGURED ALL TASK TRACKERS  #####")
