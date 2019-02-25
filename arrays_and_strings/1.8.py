input_matrix = [[0,1,2,3,1],[4,5,6,7,0],[8,9,0,11,3],[12,13,14,15,9]]
zero_matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def zero_Row(i):
	print(len(input_matrix[0]))
	for j in range(len(input_matrix[0])):
		input_matrix[i][j] = 0

def zero_Column(j):
	print(len(input_matrix))
	for i in range(len(input_matrix)):
		input_matrix[i][j] = 0
		
def zero_Matrix(input_matrix):
	
	n = len(input_matrix)
	
		
	print("Printing input array....\n")
	
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			print(input_matrix[i][j]," ", end="")
		print()
		
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			if input_matrix[i][j] == 0:
				zero_matrix[i][j] = 1
		
	
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			# print(zero_matrix[i][j]," ", end="")
			if zero_matrix[i][j] == 1:
				zero_Row(i)
				zero_Column(j)
		print()
	
	print("Printing output array....\n")
	
	for i in range(len(input_matrix)):
		for j in range(len(input_matrix[0])):
			print(input_matrix[i][j]," ", end="")
		print()
		


zero_Matrix(input_matrix)