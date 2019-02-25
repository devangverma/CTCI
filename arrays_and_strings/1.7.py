
def rotateMatrix(input_matrix):
	
	n = len(input_matrix)

	print("Printing input array....\n")
	
	for i in range(n):
		for j in range(n):
			print(input_matrix[i][j]," ", end="")
		print()
	
	for i in range(int(n/2)):
		
		for j in range(i, n-1-i):
			temp = input_matrix[i][j]
			input_matrix[i][j] = input_matrix[n-1-j][i]
			input_matrix[n-1-j][i] = input_matrix[n-1-i][n-1-j]
			input_matrix[n-1-i][n-1-j] = input_matrix[j][n-1-i]
			input_matrix[j][n-1-i] = temp
		
	print("Printing output array....\n")
	
	for i in range(n):
		for j in range(n):
			print(input_matrix[i][j]," ", end="")
		print()

input_matrix = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

rotateMatrix(input_matrix)