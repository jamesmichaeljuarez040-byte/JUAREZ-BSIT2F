# Name: JAMES MICHAEL JUAREZ
# Assessment 3.2: Linear Data Structure

# SINGLY LINKED LIST PROGRAM
# Adds every letter of a word as a node, then removes
# the nodes one by one from the head until it is empty.

class Node:
    def __init__(self, data):
        self.data = data      # the letter
        self.next = None      # link to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # add a new node at the end of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove_first(self):
        # remove the head node and return its letter
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        return self.head is None

    def show(self):
        # returns the list as: A -> B -> C -> NULL
        if self.head is None:
            return "NULL"
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return " -> ".join(parts) + " -> NULL"

# Dynamic input (press Enter to use the default name)
word = input("Enter a word (example: JUAREZ): ").upper()
if word.strip() == "":
    word = "JAMES MICHAEL JUAREZ"

linked_list = SinglyLinkedList()

# ADD: one node per letter (spaces are skipped)
for letter in word:
    if letter != " ":
        linked_list.add(letter)

print()
print("Add:", linked_list.show())

# REMOVE: delete the head node each time
while not linked_list.is_empty():
    removed = linked_list.remove_first()
    print(f"Remove {removed}: {linked_list.show()}")

if linked_list.is_empty():
    print("Result: EMPTY")
