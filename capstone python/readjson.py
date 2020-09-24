import json
import requests
import re

input_text = ''


infile = open("F:\\SmallSetTest\\split\\data\\frontup\\Classic Myths___Mary Catherine Judd___February 2006___2..dat")
data = infile.read()
split_data = re.split("entities {*}\n", data)


stringStuff = ''

#print(len(split_data[0]))

brackets = 0

out = open('outFile.txt', 'w+', errors='ignore')

for x in range(len(split_data[0])):
	if split_data[0][x] == '{':
		brackets+= 1
	if split_data[0][x] == '}':
		brackets-=1
	#if split_data[0][]
	
	if brackets == 0:
		pass
		#print('END OF ENTITY')
		#out.write('\nEND OF ENTITY')

	if split_data[0][x] != '\n':
		stringStuff += split_data[0][x]
	else:
		print(stringStuff)
		#out.write('\n' + stringStuff)
		stringStuff = ''

#try:
	#with open("F:\\SmallSetTest\\split\\data\\Classic Myths___Mary Catherine Judd___February 2006___2..json") as file:
		#print(file)
	#	input_text = json.load(file)
	#print("File loaded")
#except ValueError:
	#print(ValueError)
	#pass

#print(indict) 