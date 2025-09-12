class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


Head = Tail = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

Head.left = A
A.left = B
B.left = C
C.left = None

# Traversed

curr = Head
while curr:
    print(curr)
    curr = curr.left

# LInked List
def display(head):
    curr = head
    items = []
    while curr:
        items.append(str(curr.val))
        curr = curr.left
    print(' -> '.join(items))

display(Head)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.left

    return False

print(search(Head, 0))

# Display Double Linked List
def display(head):
    current = head
    items = []
    while current:
        items.append(str(current.val))
        current = current.left
    print(' <-> '.join(items))

display(Tail)


# Insert element
def ins(head, tail, val):
    new_head = Node(val, left=head)
    head.right = new_head
    return  new_head, tail

head, tail = ins(Head, Tail, 10)
display(head)