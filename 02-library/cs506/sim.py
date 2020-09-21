def euclidean_dist(x, y):
	if not x or not y:
		raise ValueError('lengths must not be zero')
	if len(x) != len(y):
		raise ValueError('lengths must be equal')
	sum = 0
	for i in range(len(x)):
		sum += (x[i] - y[i])**2
	return sum**(1/2)

def manhattan_dist(x, y):
	if not x or not y:
		raise ValueError('lengths must not be zero')
	if len(x) != len(y):
		raise ValueError('lengths must be equal')
	sum = 0
	for i in range(len(x)):
		if x[i] > y[i]:
			sum += x[i] - y[i]
		else:
			sum += y[i] - x[i]
	return sum

def jaccard_dist(x, y):
	if not x or not y:
		raise ValueError('lengths must not be zero')
	if len(x) != len(y):
		raise ValueError('lengths must be equal')
	diff = 0
	score = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			diff += 1
		else:
			score += 1
	return 1 - score/(score+diff)

def cosine_sim(x, y):
	if not x or not y:
		raise ValueError('lengths must not be zero')
	if len(x) != len(y):
		raise ValueError('lengths must be equal')
	vec_product = 0
	norm_x = 0
	norm_y = 0
	for i in range(len(x)):
		vec_product += x[i] * y[i]
		norm_x += x[i]**2
		norm_y += y[i]**2
	norm_product = norm_x**(1/2) * norm_y**(1/2)
	if norm_product == 0:
		raise ZeroDivisionError()
	return vec_product/norm_product


# Feel free to add more
