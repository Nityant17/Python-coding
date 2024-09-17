# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node in the list
# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None
    # Method to insert a node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list and insert the new node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    # Method to delete a node by value
    def delete(self, data):
        current = self.head
        # If the list is empty, return
        if current is None:
            print("List is empty. Nothing to delete.")
            return
        # If the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        # Traverse the list to find the node to delete
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        # If the node was not found
        if current is None:
            print(f"Node with value {data} not found.")
            return
        # Unlink the node from the list
        prev.next = current.next
        current = None
    # Method to traverse the linked list and print its elements
    def traverse(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next
# Example usage
if __name__ == "__main__":
    # Create a new LinkedList object
    linked_list = LinkedList()
    # Insert elements 10, 20, 30
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    # Delete element 20
    linked_list.delete(20)
    # Traverse the list and print the elements
    print("Linked List after operations:")
    linked_list.traverse()
