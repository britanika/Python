class LinkedList:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def add_last(self, item):
        node = self.Node(item)

        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def add_first(self, item):
        node = self.Node(item)

        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

    def index_of(self, item):
        index = 0
        current = self.first
        while current is not None:
            if current.item == item:
                return index
            else:
                current = current.next
                index += 1
        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def remove_first(self):
        if self.is_empty():
            raise Exception("LinkedList is empty.")
        if self.first == self.last:
            self.first = self.last = None
            return

        second = self.first.next
        self.first.next = None
        self.first = second

    def remove_last(self):
        if self.is_empty():
            raise Exception("LinkedList is empty.")
        if self.first == self.last:
            self.first = self.last = None
            return

        previous = self.get_previous(self.last)
        self.last = previous
        self.last.next = None

    def get_previous(self, last):
        current = self.first
        while current is not None:
            if current.next == last:
                return current
            else:
                current = current.next
        return None

    def __iter__(self):
        return self.LinkedListIterator(self)

    class LinkedListIterator:
        def __init__(self, linked_list):
            self.current = linked_list.first

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is None:
                raise StopIteration
            item = self.current.item
            self.current = self.current.next
            return item


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.add_first(1)
    linkedlist.add_first(2)
    linkedlist.add_first(3)
    linkedlist.add_last(4)
    linkedlist.add_last(5)
    linkedlist.remove_last()
    linkedlist.remove_first()
    for item in linkedlist:
        print(item)
    print(linkedlist.index_of(4))
    print(linkedlist.contains(4))
    print(linkedlist.contains(6))
