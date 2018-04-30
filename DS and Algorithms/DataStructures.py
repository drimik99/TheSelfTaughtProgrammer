# Stack 
	# LIFO property --> last in first out
	# only add and remove things from the last item

class Stack():
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

stack = Stack()
print(stack.is_empty())

# Reversing a String with a Stack
	# a stack can reverse an iterable because whatever comes off stack is in reverse order

for i in "Hello":
	stack.push(i)

reverse = ""

for i in range(len(stack.items)):
	reverse += stack.pop()

print(reverse)	# prints olleH

# Queue
	# FIFO property --> first in first out
	# only add and remove things from the first item

class Queue():
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item): # adds item to queue
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

