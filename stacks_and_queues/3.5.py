
class stack:
	def __init__(self):
		self.items = []
				
	def push(self, val):
		self.items.append(val)
	
	def pop(self):
		return self.items.pop()
	
	def isEmpty(self):
		return self.items == []
	
	def peek(self):
		return self.items[len(self.items)-1]
	
def sortStack(s1):
	s2 = stack()
	temp = 0
	
	s2.push(s1.pop())
	
	while not s1.isEmpty():
		print("s2.items",s2.items,"s1.items",s1.items)
		print("s2.peek",s2.peek(),"s1.peek",s1.peek())
		if s2.peek()>s1.peek():
			temp = s1.pop()
			while not s2.isEmpty():
				if temp < s2.peek():
					s1.push(s2.pop())
				else:
					break
			s2.push(temp)
		else:
			s2.push(s1.pop())
	while not s2.isEmpty():
		s1.push(s2.pop())
	
	return s1
	
s1 = stack()


s1.push(5)
s1.push(2)
s1.push(3)
s1.push(4)

print("s1",s1.items)

s1 = sortStack(s1)

print("s1",s1.items)
