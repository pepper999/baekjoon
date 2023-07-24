class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

string = input()

head = Node(None)
node = head

for char in string:
    # double linked list로 초기화
    new_node = Node(char, prev= node)
    node.next = new_node
    node = new_node

M = int(input())
for i in range(M):
    ip = input()
    if ip == 'L':
        if node.prev is not None:
            node = node.prev
    elif ip == 'D':
        if node.next is not None:
            node = node.next
    elif ip == 'B':
        if node.prev is not None:
            temp_node = node.prev
            temp_node.next = node.next
            if node.next is not None:
                node.next.prev = temp_node
            node = temp_node
    else:
        temp_next = node.next
        new_node = Node(ip[2], next = temp_next, prev = node)
        node.next = new_node
        if temp_next is not None:
            temp_next.prev = new_node
        node = new_node

node = head

while node.next is not None:
    node = node.next
    print(node.data, end = '')