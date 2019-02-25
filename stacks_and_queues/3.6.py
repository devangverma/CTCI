
class MyQueue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
		
	def enqueue(self, val):
		
		while len(self.stack2) > 0:
			self.stack1.append(self.stack2.pop())
		
		self.stack1.append(val)
	
	def dequeue(self):
		
		while len(self.stack1) > 0:
			self.stack2.append(self.stack1.pop())
		
		return self.stack2.pop()
		
	def peek(self):
		
		while len(self.stack1) > 0:
			self.stack2.append(self.stack1.pop())
		if len(self.stack2)-1 >= 0:
			return self.stack2[len(self.stack2)-1]
		else:
			return -1
	def isEmpty(self):
		return self.stack1 == [] and self.stack2 == []
	
class AnimalShelter:
	def __init__(self):
		self.dogs = MyQueue() #queue.Queue()
		self.cats = MyQueue()
		self.animals = MyQueue()
	
	def put(self, type, id):
		if type == "dog":
			self.dogs.enqueue(id)
		elif type == "cat":
			self.cats.enqueue(id)
		else:
			self.animals.enqueue(id)
		
	def get(self, type):
		result = None
		temp = MyQueue()
		
		if type == "dog":
			if self.dogs.peek() != -1:
				if self.dogs.peek() == self.animals.peek():
					self.dogs.dequeue()
					return self.animals.dequeue()
				else:
					while not self.animals.isEmpty():
						if self.dogs.peek() == self.animals.peek():
							result = self.animals.dequeue()
						temp.enqueue(self.animals.dequeue())
					
					self.dogs.dequeue()
				
					while not temp.isEmpty():
						self.animals.enqueue(temp.dequeue())
			else:
				print("No more dogs left.")
		elif type == "cat":
			if self.cats.peek() != -1:
				if self.cats.peek() == self.animals.peek():
					self.cats.dequeue()
					return self.animals.dequeue()
				else:
					while not self.animals.isEmpty():
						if self.cats.peek() == self.animals.peek():
							result = self.animals.dequeue()
						temp.enqueue(self.animals.dequeue())
					
					self.cats.dequeue()
				
					while not temp.isEmpty():
						self.animals.enqueue(temp.dequeue())
			else:
				print("No more cats left.")
		else:
			result = self.animals.dequeue()
			if result == self.dogs.peek():
				self.dogs.dequeue()
			elif result == self.cats.peek():
				self.cats.dequeue()
		return result
		
animal = AnimalShelter()

animal.put("dog", 1)
animal.put("", 1)
animal.put("cat", 2)
animal.put("", 2)
animal.put("cat", 3)
animal.put("", 3)
animal.put("cat", 4)
animal.put("", 4)
animal.put("dog", 5)
animal.put("", 5)
animal.put("cat", 6)
animal.put("", 6)

print("animal:",animal.get("animal"))
print("animal:",animal.get("animal"))
print("animal:",animal.get("dog"))
print("animal:",animal.get("dog"))
