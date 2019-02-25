
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node!=None:
			print(node.val)
			node = node.next
	def partition(node, n):
		
		head = node
		tail = None
		
		while node!=None:
			if node.val < n:
				temp = node.next
				node.next = head
				head = node
				node = temp
				
			else:
				if tail != None:
					tail.next = node
					tail = node
					
				else:
					tail = node
				node = node.next
				tail.next = None
			
		print("head:",str(head.val))
		return head
		
node1 = Node(12)
node2 = Node(19)
node3 = Node(18)
node4 = Node(8)
node5 = Node(7)
node6 = Node(11)
node7 = Node(1)
node8 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

print("LinkedList:")
Node.traverse(node1)

print("LinkedList:")
Node.traverse(Node.partition(node1, 8))