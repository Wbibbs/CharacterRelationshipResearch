inFile = open("F:\outCorrect.txt", 'r+')

prevType = False
commonLine = False

with open('test.txt', 'w+') as a:
	for line in inFile:
		if prevType:
			if ('type:' in line[0:5]):
				#line = str(line[0:5] + ' PERSON\n')
				line = ''
			prevType = False
			
		if ('type:' in line[0:5]):
			prevType = True
			#if ('type:' in next(inFile)[0:5]):
				#commonLine = True
	
		a.write(line)
	
