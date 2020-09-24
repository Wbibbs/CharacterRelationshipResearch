for key in list_of_keys:
	num_of_nouns += 1
	for item in master_dict[key]:

		#if key not in edges: # -- produces small edge counts
			#edges[key] =  [item]
		#else:
			#edges[key].append(item)
		
		for key2 in list_of_keys:
			for item2 in master_dict[key2]:
			
				if key not in edges: # -- produces large edge counts
					edges[key] =  [item]
				else:
					edges[key].append(item)
			
				#print(item)
				if int(str(item).strip("['']")) > int(str(item2).strip("['']")):
					if int(str(item).strip("['']")) - int(str(item2).strip("['']")) <= offset_check:
						in_string = str(key + '\t' + key2)
						if in_string not in matched_dict:
							matched_dict[in_string] = 1
						else:
							matched_dict[in_string] = matched_dict[in_string] + 1
				else:
					if int(str(item2).strip("['']")) - int(str(item).strip("['']")) <= offset_check:
						matched_dict[str(key + '\t' + key2)] = 1
						in_string = str(key + '\t' + key2)
						if in_string not in matched_dict:
							matched_dict[in_string] = 1
						else:
							matched_dict[in_string] = matched_dict[in_string] + 1
		

for key in edges:
	num_of_edges = 0
	for edge in edges[key]:
		num_of_edges += 1
	edges[key] = num_of_edges

max_edges = 0
min_edges = 0
avg_edges = 0
first_run = True
all_edges = [] #numeric value of edges

for key in edges:
	if first_run:
		max_edges = edges[key]
		min_edges = edges[key]
		avg_edges = edges[key]
		first_run = False
	else:
		if edges[key] > max_edges:
			max_edges = edges[key]
		if edges[key] < min_edges:
			min_edges = edges[key]
		all_edges.append(edges[key])
		
count = 0
total = 0
for num in all_edges:
	total += num
	count += 1

avg_edges = total / count