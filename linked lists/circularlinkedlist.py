class Element(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class CircularLinkedList(object):
    def __init__(self, head=None)-> None:
        self.head = head

    def insertAtTheBeggining(self, new_element):
        current = self.head
        if current.next:
            while current.next != self.head:
                current = current.next

            new_element.next = self.head
            self.head = new_element
            current.next = self.head
        else:
            new_element.next = self.head
            self.head = new_element

    def printLinkedList(self):
        head = self.head
        current = head.next
        while current != head:
            print(current.value)
            current = current.next
        
            
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


ll = CircularLinkedList(e1)
ll.insertAtTheBeggining(e2)
ll.printLinkedList()