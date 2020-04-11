matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]

def add(*args):
	for matrix in args:
		for row in matrix:
			if len(matrix) != len(args[0]) or len(row) != len(args[0][0]):
				raise ValueError('Given matrices are not the same size.')
	return [
		[
			sum(b)
			for b in zip(*a)
		]
		for a in zip(*args)
	]

print(add(matrix1, matrix2))