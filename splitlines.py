import os
from itertools import islice
directory = "D:\\CapstoneDataSplit\\test data\\"

#for file in os.listdir(directory):
#	text = open(str(directory + file), "r+")
	#for line in enumerate(text):
	#	if 

num = 0
for file in os.listdir(directory):
	T = open(str(directory + file), "r+", errors="ignore")
	out = open(str(directory + file + str(num )+ ".part"), "w+", errors="surrogateescape")
	for i, sli in enumerate(iter(lambda:list(islice(T, 300)), []), 1):
		with open(str(directory + file + str(num )+ ".part"), "w") as f:
			out.writelines(sli)
	num += 1