
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
	
mq = MyQueue()

print("stack1",mq.stack1, "stack2",mq.stack2)
mq.enqueue(1)
print("stack1",mq.stack1, "stack2",mq.stack2)
mq.enqueue(2)
print("stack1",mq.stack1, "stack2",mq.stack2)
mq.enqueue(3)
print("stack1",mq.stack1, "stack2",mq.stack2)

mq.dequeue()
print("stack1",mq.stack1, "stack2",mq.stack2)
mq.dequeue()
print("stack1",mq.stack1, "stack2",mq.stack2)

mq.enqueue(4)
print("stack1",mq.stack1, "stack2",mq.stack2)