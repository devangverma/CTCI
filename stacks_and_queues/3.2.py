
class stack:
	
	def __init__(self):
		self.items = []
		self.min = [100000]
	
	def isEmpty(self):
		return self.items == []
	
	def push(self, val):
		self.items.append(val)
		
		if self.min[len(self.min)-1] > val:
			self.min.pop()
			self.min.append(val)
	
	def peek(self):
		return self.items[len(self.items)-1]

	def getMin(self):
		return self.min[len(self.min)-1]	
		
	def pop(self):
		if self.min[len(self.min)-1] == self.items[len(self.items)-1]:
			self.min.pop()
			
		return self.items.pop()
		
s = stack()

print("isEmpty:",s.isEmpty())
print("getMin:",s.getMin())
s.push(1)
s.push(2)
s.push(3)
print("isEmpty:",s.isEmpty())
print("getMin:",s.getMin())
print("pop:",s.pop())
print("pop:",s.pop())
print("isEmpty:",s.isEmpty())
print("getMin:",s.getMin())

