
class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node != None:
			print(node.val)
			node = node.next
		
def removeDups(node):
	l = set()
	
	previous = node
	
	while node != None:
		if node.val in l:
			print("Remove",str(node.val))
			previous.next = node.next
			
			
		else:
			l.add(node.val)
			print("Add",str(node.val))
			previous = node
		
		node = node.next
		print(l)
		
node1 = Node(12)
node2 = Node(15)
node3 = Node(12)
node4 = Node(16)
node5 = Node(12)
node6 = Node(17)
	
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("LinkedList:")
Node.traverse(node1)

removeDups(node1)

print("LinkedList:")
Node.traverse(node1)

