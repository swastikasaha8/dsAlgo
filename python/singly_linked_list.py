class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, *args) -> None:
        self.head = Node(None)
        prevNode = self.head
        for i in args:
            newNode = Node(i)
            newNode.next = None
            prevNode.next = newNode
            prevNode = newNode

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
            if newNode.next is None:
                self.lastNode = newNode

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

    def popAt(self, pos: int) -> None:
        node = self.head
        prevNode = node
        for i in range(pos):
            prevNode = node
            if node is not None:
                node = node.next
        try:
            node = node.next
            tempNode = prevNode.next
            del tempNode
            prevNode.next = node
        except:
            print("You cannot delete an element outside the range of the linked list")

    def search(self, data) -> str:
        node = self.head.next
        pos = 1
        positions = []
        while node is not None:
            if node.data == data:
                positions.append(str(pos))
            if node.next is not None:
                node = node.next
                pos += 1
            else:
                pos = "Sorry, this item doesn't exist in the linked list"
                break

        if len(positions) > 1:
            return f"Position of '{data}' in list are {' and '.join(positions)}!"
        elif len(positions) > 0:
            return f"Position of '{data}' in list is {positions[0]}!"
        else:
            return "Sorry this element doesn't exist in the list :("

    def __str__(self):
        nodes = []
        node = self.head.next
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        linkedList = " -> ".join(nodes)
        return f"Linked List : {linkedList}"


newLinkedList = LinkedList("a", "d", "c", "d", "e", "f")
print(newLinkedList)
