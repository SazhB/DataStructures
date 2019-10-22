class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def getNode(self):
        return self.val


class Queue:
    def __init__(self, node):
        self.head = Node(node)

    def append(self, val):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(val)

    def _Queue(self, Queue):
        head = Queue.head
        Queue.head = head.next
        return Queue

    def display(self):
        cur = self.head
        while cur.next != None:
            print (cur.val)
            cur = cur.next
        print (cur.val)
