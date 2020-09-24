with open("F:\\nov5\\listoftexts.txt", 'r+', encoding='utf8') as text:
	all_lines = []
	
	for line in text:
		if line not in all_lines:
			all_lines.append(line)
			
	out = open("F:\\nov5\\listoftextsnodupes.txt", 'w+', encoding='utf8')
	for line in text:
		out.write(line)
	out.close()
	