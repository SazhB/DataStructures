def main

class Tree:

    class Node:
        def __init__(self, left = None, right, None):
            self.left = left
            self.right = right

    def __init__(self, head=None):
        self.head = None

    def add_branch(self, value):
        self.head = Tree._add_branch(self.head, value)

    def _add_branch(head, val):
        if head == None:
            return Tree.Node(value)



    def pop_branch(self):
        cur = self.head
        branch = False
        while not False:
            if cur.next != None:
                cur = cur.next
            else:
                holder = cur
                cur = None
                return holder

    def get_first_branch(self):
        return self.head

    def print_tree(self):
        branch = False
        cur = self.head
        while not branch:
            print (cur)
            if cur.next != None:
                cur = cur.next
            else:
                branch = True



if __name__ == "__main__":
