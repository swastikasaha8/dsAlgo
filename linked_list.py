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

    def push(self, data) -> None:
        newNode = Node(data)
        newNode.next = None
        self.lastNode.next = newNode
        self.lastNode = newNode

    def insert(self, data, pos: int) -> None:
        node = self.head
        prevNode = node
        for i in range(pos):
            prevNode = node
            if node is not None:
                node = node.next
        try:
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode
        except:
            print("Sorry You cannot insert an element outside the linked list")

    def pop(self) -> None:
        if self.head.next is None:
            print("You cannot remove items from an empty linked list")
        else:
            node = self.head
            prevNode = node
            while node.next is not None:
                prevNode = node
                node = node.next
            del node
            prevNode.next = None
            self.lastNode = prevNode

    def popAt(self, pos: int = -1) -> None:
        pass

    def __str__(self):
        nodes = []
        node = self.head.next
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        linkedList = " -> ".join(nodes)
        return linkedList


newLinkedList = LinkedList("a", "c", "d")
newLinkedList.insert(2.5, 4)
print(newLinkedList)
