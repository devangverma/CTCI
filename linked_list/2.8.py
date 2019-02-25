
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
	
	def loopDetection(node):
		
		fast = node
		slow = node
		
		while fast!= None:
			fast = fast.next.next
			slow = slow.next
			
			if fast == slow:
				break
		
		if fast == None:
			print("no loop")
			return
		slow = node
		
		while fast != None:
			if fast == slow:
				print("loop starts here:", slow.val)
				return
			fast = fast.next
			slow = slow.next	
			
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

Node.loopDetection(node1)