
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def size(node):
		len =0
		while node!= None:
			len+=1
			node = node.next
		return len
		
	def traverse(node):
		
		while node != None:
			print(node.val)
			node = node.next
	
	def intersection(node1, node2):
		
		new_node1 = node1
		new_node2 = node2
		
		if Node.size(node1) != Node.size(node2):
			if Node.size(node1) < Node.size(node2):
				new_node1 = node2
				new_node2 = node1
			i = abs(Node.size(node1) - Node.size(node2))
			while i > 0:
				new_node1 = new_node1.next
				i-=1
		
		while new_node1 != new_node2:
			new_node1 = new_node1.next
			new_node2 = new_node2.next
		
		if new_node1 == None and new_node2 == None:
			print("No intersection.")
		else:
			print("Intersection.")
	
node11 = Node(1)
node12 = Node(2)
node13 = Node(3)
node14 = Node(4)
node21 = Node(5)
node22 = Node(6)

node5 = Node(9)
node6 = Node(10)
node7 = Node(11)
node8 = Node(12)

node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node5
node21.next = node22
node22.next = node5

node5.next = node6
node6.next = node7
node7.next = node8

print("LinkedList#1:")
Node.traverse(node11)

print("LinkedList#2:")
Node.traverse(node21)

print("Size#1:", int(Node.size(node11)))

print("Size#2:", int(Node.size(node21)))

Node.intersection(node11, node21)