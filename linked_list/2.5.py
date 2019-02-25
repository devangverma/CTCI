
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def traverse(self):
		node = self
		
		while node != None:
			print(node.val)
			node = node.next

	def sumNumbers(node1, node2, carry):
		
		temp = carry
		
		if node1 != None:
			temp+=node1.val
		if node2 != None:
			temp+=node2.val
			
		if temp > 9:
			node1.val=temp%10
			carry = 1 
		else:
			print("node1:",node1.val)
			node1.val = temp
			carry = 0
			
		if node1.next == None and node2.next == None:
			if carry > 0 :
				new_node = Node(carry)
				node1.next = new_node
			
		else:
			Node.sumNumbers(node1.next, node2.next, carry)
		
			
			
node1_number1 = Node(1)
node2_number1 = Node(2)
node3_number1 = Node(3)

node1_number1.next = node2_number1
node2_number1.next = node3_number1

node1_number2 = Node(6)
node2_number2 = Node(5)
node3_number2 = Node(4)

node1_number2.next = node2_number2
node2_number2.next = node3_number2

print("first number:")
Node.traverse(node1_number1)

print("second number:")
Node.traverse(node1_number2)

print("final sum:")
Node.sumNumbers(node1_number1, node1_number2, 0)
Node.traverse(node1_number1)