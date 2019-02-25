
class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node != None:
			print(node.val)
			node = node.next
	
	def size(node):
		len = 0
		while node != None:
			len+=1
			node = node.next
		return len
		
	def reverse(node):
		head = node
		previous = node
		current = previous.next
		
		while current != None:
			temp = current.next
			current.next = head
			previous.next = temp
			head = current
			current = temp
						
		return head
	
	def merge(node1, middle, node2, size):
		i = 0 
		
		print("first1:")
		Node.traverse(node1)
		print("second1:")
		Node.traverse(node2)
			
		while node1.next != None:
			node1 = node1.next
			
		if middle != None:	
			node1.next = middle
			middle.next = node2
		else:
			node1.next = node2
		
	def palindrome(node):
		size = Node.size(node)
		head1 = node
		node1 = head1
		
		if size%2 == 0:
			i = 0
			while i < (size/2)-1:
				node = node.next
				i+=1
			head2 = node.next
			node.next = None
						
			node2 = Node.reverse(head2)
			head2 = node2
			
			print("first:")
			Node.traverse(head1)
			print("second")
			Node.traverse(node2)

			while node1 != None and node2 != None:
				if node1.val != node2.val:
					print("Not a palindrome.")
					head2 = Node.reverse(head2)
					Node.merge(head1, None, head2, size)
					return
				node1 = node1.next 
				node2 = node2.next
			print("Palindrome.")
			head2 = Node.reverse(head2)
			Node.merge(head1, None, head2, size)
		
		else:
			i = 0
			while i < (size/2)-2:
				node = node.next
				i+=1
			middle = node.next
			
			head2 = node.next.next
			middle.next = None
			node.next = None
						
			node2 = Node.reverse(head2)
			head2 = node2
			
			print("first:")
			Node.traverse(head1)
			print("second")
			Node.traverse(node2)

			while node1 != None and node2 != None:
				if node1.val != node2.val:
					print("Not a palindrome.")
					head2 = Node.reverse(head2)
					Node.merge(head1, middle, head2, size)
					return
				node1 = node1.next 
				node2 = node2.next
			print("Palindrome.")
			head2 = Node.reverse(head2)
			Node.merge(head1, middle, head2, size)
			
	
node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

print("Input")
Node.traverse(node1)

Node.palindrome(node1)

print("Output")
Node.traverse(node1)
