
class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node != None:
			print(node.val)
			node = node.next
	
	def deleteMiddleNode(node):
		node.val = node.next.val
		node.next = node.next.next
	
node1 = Node(12)
node2 = Node(13)
node3 = Node(14)
node4 = Node(15)
node5 = Node(16)
node6 = Node(17)
node7 = Node(18)
node8 = Node(19)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

print("LinkedList:")

Node.traverse(node1)

Node.deleteMiddleNode(node3)

print("LinkedList:")

Node.traverse(node1)