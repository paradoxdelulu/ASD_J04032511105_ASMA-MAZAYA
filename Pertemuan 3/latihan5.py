#================================================================================================================
# Latihan 5 :
# Tambahkan	metode	untuk	membalik	(reverse)	sebuah	single	linked	list tanpa membuat linked list baru.
# ================================================================================================================

class Node:
    def	__init__(self, data):	
        self.data = data	
        self.next = None

class LinkedList:
    def	__init__(self):	
        self.head =	None

    def append(self, new_data):    
        new_node = Node(new_data)	
        if self.head is None:	
            self.head = new_node	
            return	
        last = self.head	
        while last.next:	
            last = last.next	
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")	

# ================= TEST =================
# Contoh Tampilan 1 :
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Original Linked List:")
ll.display()
ll.reverse()

print("Reversed Linked List:")
ll.display()

#Contoh Tampilan 2 :
ll2 = LinkedList()
ll2.append(10)
ll2.append(20)
ll2.append(30)
ll2.append(40)

print("Original Linked List:")
ll2.display()
ll2.reverse()

print("Reversed Linked List:")
ll2.display()

#Contoh Tampilan 3 :
ll3 = LinkedList()
ll3.append(7)

print("Original Linked List:")
ll3.display()
ll3.reverse()

print("Reversed Linked List:")
ll3.display()

