class Stack_Node:
    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, node_data):
        node = Stack_Node(data=node_data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.down = self.head
            node.up = None

            self.head.up = node
            self.head = node

    def pop(self):
        item = -1
        if self.head:
            if self.head == self.tail:
                item = self.head.data
                old_head = self.head
                old_tail = self.tail
                self.head = None
                self.tail = None
                del old_head
                del old_tail
            else:
                new_head = self.head.down
                new_head.up = None
                old_head = self.head
                item = old_head.data
                self.head = new_head
                del old_head
        return item
    
    def is_empty(self):
        return self.head is None and self.tail is None
    
# testing stacks
# stack = Stack()
# for i in range(4):
#     stack.push(i)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
# head = stack.head
# while head:
#     print(head.data, end=",")
#     head = head.down

# for i in range(4):
#     stack.push(i)
#     head = stack.head
# while head:
#     print(head.data, end=",")
#     head = head.down


class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, node_data):
        self.enqueue_stack.push(node_data)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    
    def peek(self):
        node_data = self.dequeue()
        self.dequeue_stack.push(node_data)
        return node_data


q = int(input("Enter the number of queries: "))
queue = Queue()
for _ in range(q):
    query = list(map(int, input("Enter the action [add=1 remove=2 peek=3] and number if adding to queue: ").split()))
    
    action = query[0]
    
    if query[0] == 1:  # add element to queue
        queue.enqueue(query[1])
    elif query[0] == 2:  # remove element from queue
        queue.dequeue()
    else:  # print element at front of queue
        print(queue.peek())



# Input (stdin)

#     10

#     1 76

#     1 33

#     2

#     1 23

#     1 97

#     1 21

#     3

#     3

#     1 74

#     3

# Expected Output

#     33

#     33

#     33



# Input (stdin)

#     10

#     1 42

#     2

#     1 14

#     3

#     1 28

#     3

#     1 60

#     1 78

#     2

#     2

# Expected Output

#     14

#     14