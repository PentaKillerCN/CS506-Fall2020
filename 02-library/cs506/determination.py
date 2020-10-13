def determination(A):
	if not A:
		raise ValueError('Non Empty Matrix Expected')
	for row in A:
		if len(A) != len(row):
			raise ValueError('Square Matrix Expected')
	if len(A) == 1:
		return A[0][0]
	if len(A) == 2:
		ad = A[0][0]*A[1][1]
		bc = A[0][1]*A[1][0]
		return ad-bc
	ret = 0
	sign = 1
	for col in range(len(A[0])):
		ret += sign*A[0][col]*determination(matrix_excluded_col(A, col))
		sign *= -1
	return ret


def matrix_excluded_col(A, excluded_col):
	if not A:
		raise ValueError('Non Empty Matrix Expected')
	for row in A:
		if len(A) != len(row):
			raise ValueError('Square Matrix Expected')
	size = len(A)-1
	ret = [[]*size for i in range(size)]
	for row in range(1, len(A)):
		for col in range(len(A[row])):
			if col == excluded_col:
				continue
			ret[row-1].append(A[row][col])
	return ret
