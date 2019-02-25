
class Tree:
	def __init__(self, val):
		self.data = val
		self.right = None
		self.left = None
	
def minimalTree(root, array, i, j, right):
	
	if i >= 0 and j<len(array) and i<=j:
		if i != j:
			val = array[int((i+j)/2)]
			node = Tree(val)
			if right == 1:
				root.right = node
			else:
				root.left = node
			
			minimalTree(node, array, i, int((i+j)/2)-1, 1)
			minimalTree(node, array, int((i+j)/2)+1, j, 0)
		if i == j:
			val = array[i]
			node = Tree(val)
			if right == 1:
				root.right = node
			else:
				root.left = node
			
			node.right = None
			node.left = None
				
		
	else:
		return 
		
def buildTree(root, array):
	
	minimalTree(root, array, 0, int(len(array)/2)-1, 1)
	minimalTree(root, array, int(len(array)/2)+1, len(array)-1, 0)
	
		
def traverse(root):
	node = root
	if node.right != None:
		traverse(node.right)
	print(node.data)
	if node.left != None:
		traverse(node.left)

if __name__ == "__main__":			
	arr = [1,2,3,4,5,6,7,8,9]

	size = len(arr)
	val = arr[int(size/2)]
	root = Tree(val)

	buildTree(root, arr)
	traverse(root)