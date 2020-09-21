def read_csv(csv_file_path):
	"""
	    Given a path to a csv file, return a matrix (list of lists)
	    in row major.
	"""
	ret = []
	file = open(csv_file_path, 'r')
	lines = file.readlines()
	for line in lines:
		list_of_strings = line.split(',')
		list_of_values = []
		for item in list_of_strings:
			try:
				v = int(item)
				list_of_values.append(v)
			except ValueError:
				try:
					v = float(item)
					list_of_values.append(v)
				except ValueError:
					v = item.strip("\"")
					list_of_values.append(v)
		ret.append(list_of_values)

	return ret