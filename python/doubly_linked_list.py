class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, *args) -> None:
        self.head = Node(None)
        self.head.prev = None

    def push(self):
        pass

    def pushAt(self):
        pass

    def insert(self):
        pass

    def pop(self):
        pass

    def popAt(self):
        pass

    def __str__(self) -> str:
        return "pass"
def add(x,y):
    sum=x+y