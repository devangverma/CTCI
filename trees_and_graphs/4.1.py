import queue

class Graph:
	def __init__(self, val):
		self.data = val
		self.children = []
		self.visited = False
 
def RouteBetweenNodes(node1, node2):
	# node = root
	que = queue.Queue()
		
	node1.visited = True
	que.put(node1)
	
	while not que.empty():
		temp = que.get()
		# temp.visited = True
		if temp == node2:
			print("Route exists.")
			return
		print(temp.data)
		
		for n in temp.children:
			if n.visited == False:
				print("n.data:",n.data)
				n.visited = True
				que.put(n)
	print("Route doesn't exists.")
	return		

if __name__ == "__main__":	
	node0 = Graph(0)
	node1 = Graph(1)
	node2 = Graph(2)
	node3 = Graph(3)
	node4 = Graph(4)
	node5 = Graph(5)
	node6 = Graph(6)
	# Node6 = Graph(9)

	node0.children.append(node1)
	node0.children.append(node2)
	node0.children.append(node5)

	node1.children.append(node3)
	node1.children.append(node4)

	node2.children.append(node3)
	node2.children.append(node4)

	node4.children.append(node5)
	node3.children.append(node5)

	RouteBetweenNodes(node0, node5)


