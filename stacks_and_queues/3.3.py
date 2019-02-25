
class stack:
	
	def __init__(self):
		self.stack = []
		
	def isEmpty(self):
		return self.stack == []
	
	def push(self, val):
		self.stack.append(val)
	
	def pop(self):
		return self.stack.pop()
	
	def peek(self):
		return self.stack[len(self.stack)-1]
	
	def size(self):
		return len(self.stack)

class stacks:
	def __init__(self):
		self.stacks = []
		self.noOfstacks = 0
		# self.itemsOnStack = 0
	
	def size(self):
		return len(self.stacks)
		
	def newStack(self):
		
		self.stacks.append(stack())
		self.noOfstacks += 1
		# self.itemsOnStack = 0
		print("stackNo:",self.noOfstacks, "itemsOnStack:",self.stacks[self.noOfstacks-1].size())
	
	def push(self, val):
		
		if self.stacks[self.noOfstacks-1].size() > 3:
			self.newStack()
		# self.itemsOnStack += 1
		self.stacks[self.noOfstacks-1].push(val)
		print("Push stackNo:",self.noOfstacks, "itemsOnStack:",self.stacks[self.noOfstacks-1].size(), "val:", val)
	
	def pop(self):
		print("Pop stackNo:",self.noOfstacks, "itemsOnStack:",self.stacks[self.noOfstacks-1].size())
		# self.itemsOnStack -= 1
		if len(self.stacks) > 0:
			print("len(self.stacks):",len(self.stacks))
			if self.stacks[self.noOfstacks-1].size() > 0:
				return self.stacks[self.noOfstacks-1].pop()
			else:
				print("pop else: len(self.stacks):",len(self.stacks))
				if len(self.stacks) > 1:
					self.stacks.pop()
					self.noOfstacks -= 1
					self.stacks[self.noOfstacks-1].pop()
		else:
			print("Stacks are already empty")
s = stacks()

s.newStack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
			
s.pop()
s.pop()
s.push(7)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()