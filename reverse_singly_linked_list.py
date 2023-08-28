class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)

    print("Original Linked List:")
    linked_list.display()

    linked_list.reverse()

    print("Reversed Linked List:")
    linked_list.display()
