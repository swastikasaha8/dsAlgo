class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, *args) -> None:
        self.head = Node(None)
        self.nodes = args
        self.lastNode = None
        for i in self.nodes:
            if self.head.next is None:
                self.lastNode = Node(i)
                self.lastNode.next = None
                self.head.next = self.lastNode
            else:
                newNode = Node(i)
                newNode.next = None
                self.lastNode.next = newNode
                self.lastNode = newNode

    def push() -> None:
        pass

    def insert(pos: int = -1) -> None:
        pass

    def pop() -> None:
        pass

    def popAt(pos: int = -1) -> None:
        pass

    def __str__(self):
        nodes = []
        node = self.head.next
        while node.next is not None:
            nodes.append(node.data)
            node = node.next
        linkedList = " -> ".join(nodes) + " -> " + node.data
        return linkedList


newLinkedList = LinkedList("a", "b")
print(newLinkedList)
