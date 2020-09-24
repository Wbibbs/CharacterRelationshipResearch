import re

full_text = ''

with open('a.txt', 'r+') as t:
	for line in t:
		full_text += line


out = open('out.txt', 'w+')

full_text = full_text.replace("\n", '')
print(full_text)
re.sub(r'.*START OF THIS PROJECT GUTENBERG EBOOK', ' ', full_text)

print(full_text,' NEW TEXT WRITTEN')

out.write(full_text)