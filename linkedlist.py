class Element(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def appendInTheBeggining(self, new_element):
        current = self.head
        self.head = new_element
        self.head.next = current

    def appendInTheEnd(self, new_element):
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element

    def appendInPosition(self, new_element, position):
        counter = 1
        current = self.head
        while counter < position:
            counter += 1
            previous = current
            current = current.next
        previous.next = new_element
        new_element.next = current

    def deleteFromBeggining(self):
        self.head = self.head.next

    def deleteFromEnd(self):
        current = self.head
        while current.next:
            previous = current
            current =  current.next
        previous.next = None

    def deleteFromValue(self, value):
        current = self.head
        while current.value != value:
            previous = current
            current = current.next        
        
        previous.next = current.next

    def getPositionFromValue(self, value):
        current = self.head
        counter = 1
        while current.value != value:
            counter += 1
            current = current.next
        
        counter = str(counter)
        print('Your element is in the ' + counter + ' position!')
        
    def linkedListLength(self):
        counter = 0
        current = self.head
        while current:
            current = current.next
            counter += 1
        print(counter)

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


ll = LinkedList(e1)
ll.appendInTheEnd(e2)
ll.appendInTheEnd(e3)
ll.appendInTheEnd(e4)
ll.getPositionFromValue(3)
ll.printLinkedList()