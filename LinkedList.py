class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def append(self, value):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(value)

    def delete(self, index):
        if index > self.length():
            print ("Index is not in range of the length of List")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def length(self):
        cur = self.head
        _length = 0
        while cur.next != None:
            _length += 1
            print (_length)
            cur = cur.next
        return _length
            

    def insert(self, value, index):
        if self.index > self.length():
            print ("Index is too large. Length of LinkedList: " + str(self.length()))
            return None
        cur_idx = 0
        prev_node = self.head
        cur = prev_node.next
        while cur.index != index:
            if cur.next != None: 
                while cur_idx + 1 != index:
                        prev_node = cur
                        cur = cur.next
                        cur_idx += 1

        prev_node.next = Node(value)
        prev_node = prev_node.next
        prev_node.next = cur

        if prev_node.next == None:
            prev_node.next = Node(value)



    def display(self):
        cur = self.head
        print (cur.val)
        while cur.next != None:
            cur = cur.next
            print (cur.val)


my = LinkedList(3)
my.append(5)
my.append(4)
my.append(10)
my.insert(4,0)

