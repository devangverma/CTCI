
class LinkedListNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class Tree:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
	
	def inOrderTraversal(self, root):
		node = root
		if node.right != None:
			self.inOrderTraversal(node.right)
		print(node.data)
		if node.left != None:
			self.inOrderTraversal(node.left)

class ListOfDepths:
	def __init__(self,list):
		self.list = list
	
	def listOfDepths(self, list, level, node):
		if node == None:
			return
		
		temp_node = LinkedListNode(node.data)
		
		if level+1 > len(list) :
			list.append(temp_node)
		else:
			temp = list[level]
			while temp.next != None:
				temp = temp.next
			temp.next = temp_node
			
		if node.right != None:
			self.listOfDepths(list, level+1, node.right)
		
		if node.left != None:
			self.listOfDepths(list, level+1, node.left)
	
	def traverseLinkedList(self, node):
		while node != None:
			print(node.data, " ",end='')
			node = node.next
	def traverse(self, list):
		
		for i in range(len(list)):
			temp_node = list[i]
			self.traverseLinkedList(temp_node)
			print()

if __name__ == "__main__":	
	root = Tree(6)

	Node1 = Tree(2)
	Node2 = Tree(3)
	Node3 = Tree(5)
	Node4 = Tree(7)
	Node5 = Tree(8)
	Node6 = Tree(9)

	root.right = Node2
	root.left = Node5

	Node2.right = Node1
	Node2.left = Node3

	Node5.right = Node4
	Node5.left = Node6

	root.inOrderTraversal(root)
			
	list = []

	lod = ListOfDepths(list)

	lod.listOfDepths(list, 0, root)

	print("List of depths:")
	lod.traverse(list)		
	