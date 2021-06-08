class Element(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def appendInTheBeggining(self, new_element):
        head = self.head
        self.head = new_element
        new_element.next = head
        head.previous = new_element
        new_element.previous = None

    def deleteFromEnd(self):
        current = self.head
        while current.next:
            previous = current
            current =  current.next
        previous.next = None

    def printList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


ll = LinkedList(e1)
ll.appendInTheBeggining(e2)
ll.appendInTheBeggining(e3)
ll.appendInTheBeggining(e4)
ll.deleteFromEnd()
ll.printList()