class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def isCycle(self):
        s = self.head
        f = self.head

        while f and f.next:
            s = s.next
            f = f.next.next
        
            if s == f:
                return True
        return False



if __name__ == '__main__':
    values = list(map(int, input().split()))
    
    l = LinkedList()
    for val in values:
        l.insert(val)
    
    print("Original Linked List:")
    l.display()
    
    l.reverse()
    
    print("Reversed Linked List:")
    l.display()

    print("Cycle Detection")
    print(l.isCycle())
