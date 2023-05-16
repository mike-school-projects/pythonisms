class Node:
    def __init__(self, value=None):
        self.next = None
        self.previous = None
        self.value = value

    def __str__(self):
        return str(self.value)


class SuperLinkedList:
    '''
    Super Linked List (SLL)
    SLL is a doubly-linked list
    SLL is iterable
    Added __len__ method
    Printing SLL outputs a list of values
    '''
    def __init__(self):
        self.head = None
        self.end = self.head

    def add(self, value):
        node = Node(value)

        # if empty ll, set head to node
        if self.head == None:
            node.previous = self.head
            node.next = None
            self.head = node
            self.end = node
            return

        # Not empty ll
        # connect end to this node
        node.previous = self.end
        node.next = None
        self.end.next = node
        self.end = node

    def __str__(self):
        output_list = list()
        current = self.head
        while current:
            output_list.append(str(current))
            # print(current)
            # input("wait")
            current = current.next
        return str(output_list)

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next
            return value


ll = SuperLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
print(len(ll))

