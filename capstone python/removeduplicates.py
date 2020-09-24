#This program moves Project Gutenberg duplicates, denoted by a - in their name, from input_path to output_path

import os
import shutil

input_path = "F:\\MasterNonDupe\\"
output_path = "F:\\duplicates\\"

for file in os.listdir(input_path):		
	pos = file.find('-')
	
	if pos != -1:
		os.replace(str(input_path + file), str(output_path + file))
