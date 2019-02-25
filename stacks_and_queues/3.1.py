
class stack:
	stackSize = 0
	numberOfStacks = 3
	stackCapacity = 0
	values = []
	sizes = [0]*numberOfStacks
	
	def __init__(self, stackSize):
		self.stackSize = stackSize
		self.stackCapacity = self.numberOfStacks*stackSize
		self.values = [None] * self.stackCapacity
		self.sizes = [0] * self.numberOfStacks
	
	def isEmpty(self, stackNum):
		return 0 if self.sizes[stackNum]!=0 else 1
		
	def push(self, val, stackNum):
		
		if self.sizes[stackNum] < self.stackSize:
			i = 0 if self.sizes[stackNum]== 0 else self.sizes[stackNum]-1
			self.values[i+(stackNum*self.stackSize)] = val
			self.sizes[stackNum]+=1
	
	def pop(self, stackNum):
		
		offset = stackNum*self.stackSize
		i = offset + self.sizes[stackNum]-1
		result = self.values[i]
		self.values[i] = None
		self.sizes[stackNum] -= 1
		
		return result
		
	def peek(self, stackNum):
		
		offset = stackNum*self.stackSize
		i = offset + self.sizes[stackNum]-1
		result = self.values[i]

		return result
		
s = stack(9)

print("array:",s.values)
print("isEmpty:",s.isEmpty(2))

s.push(1,0)
s.push(2,1)
s.push(3,2)
print("isEmpty:",s.isEmpty(0))
print("array:",s.values)

print("pop:",int(s.pop(2)))
print("array:",s.values)

print("peek:",int(s.peek(1)))
print("array:",s.values)