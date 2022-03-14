# Doubly linked list

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begining(self,data):
        if not self.head:
            node = Node(data)
            self.head = node
            self.tail = node
            return

        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node

    def print_forward(self):
        if self.head is None:
            print("Empty doubly liked list!")
            return
        itr = self.head
        dllist = ""
        while itr:
            dllist += str(itr.data) + "-->"
            itr = itr.next
        print(dllist)
    
    def print_backward(self):
        if self.tail is None:
            print("Empty linked list!")
            return

        itr = self.tail
        ddlist = ""

        while itr:
            ddlist += str(itr.data) + "-->"
            itr = itr.prev
        
        print(ddlist)


if __name__ == "__main__":
    dli = DoublyLinkedList()
    dli.insert_at_begining(1)
    dli.insert_at_begining(2)

    dli.print_forward()
    dli.print_backward()