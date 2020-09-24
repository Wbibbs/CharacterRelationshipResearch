import os
import queue
inDirectory = "F:\\SmallSetTest\\split\data\\frontupoutcleaned\\test"
outDirectory = "F:\\SmallSetTest\\split\\data\\frontupoutcleaned\\"

files = dict()


#	Creates a dict of queues for all files with same name, different number
for file in os.listdir(inDirectory):
	file = file[:-5] # remove ..dat extension
	
	try:
		if file[len(file)-1] == '0': # check if last digit is 0, implying first file
			q = queue.Queue()
			q.put(file + '..dat')
			files[file[:-4]] = q
		else:
			#if 
			files[file[:-4]].put(str(file + '..dat'))
	except Exception as e:
		print(e)

# Iterates through master dictionary of file's queues -- tried to implement, not sure if there's time
"""
for file in files:
	filname = ''
	firstFile = True
	for q in range(files[file].qsize()):
		print(files[file].get())
		working_filename = files[file].get()[:-10]
		
		if working_filename not in filename:
			filename = working_filename
		else:
			if firstFile:
				firstFile = False
				with open(str(filename), "w+") as out:
					with 
					
					
				
			for q in range(files[file].qsize()):
				with open(filename, "r+") as in_data:
					
"""