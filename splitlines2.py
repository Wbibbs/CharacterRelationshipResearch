import os
from itertools import islice
directory = "F:\\SmallSetTest\\"

#for file in os.listdir(directory):
#	text = open(str(directory + file), "r+")
	#for line in enumerate(text):
	#	if 

num = 0
#for file in os.listdir(directory):
#	T = open(str(directory + file), "r+", errors="ignore")
#	out = open(str(directory + file + str(num )+ ".part"), "w+", errors="surrogateescape")
#	for i, sli in enumerate(iter(lambda:list(islice(T, 300)), []), 1):
	#	with open("split_{}.txt".format(i), "w") as f:
	#		out.writelines(sli)
	#num += 1
	
for file in os.listdir(directory):
	num = 0
	if not os.path.isdir(file):
		with open(str(directory + file), "r+", errors="ignore") as T:
			for i, sli in enumerate(iter(lambda:list(islice(T, 1000)), []), 1):
				with open(str(directory + file[:len(file)-4] + "___" + str(num) + ".part") , "w+", errors="ignore") as f:
					f.writelines(sli)
				num += 1