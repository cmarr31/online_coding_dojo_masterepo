def multiplication_table():
	x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	for number in x:
		count = 1
		while count <= len(x):
			print number * count
			count +=1
multiplication_table()