
class Node:
	
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node != None:
			print(node.val)
			node = node.next
	
	def removeKthToLast(node, k):
	
		first_pointer = node
		second_pointer = node
		i = 0
		
		while i <k:
			second_pointer = second_pointer.next
			i+=1
		
		while second_pointer != None:
			first_pointer = first_pointer.next
			second_pointer = second_pointer.next
			
		print("Kth From last: ",str(first_pointer.val))		

node1 = Node(12)
node2 = Node(14)
node3 = Node(15)
node4 = Node(16)
node5 = Node(17)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("LinkedList:")
Node.traverse(node1)

Node.removeKthToLast(node1, 4)

