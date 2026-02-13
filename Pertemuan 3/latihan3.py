#==================================================================
# Latihan 3 :
# Implementasikan Pencarian pada node tertentu Double Linked List.
#==================================================================

class Node:
    def	__init__(self, data):	
        self.data = data	
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node.prev = last

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# ========== TEST ==========
dll = DoublyLinkedList()
dll.append(2)
dll.append(6)
dll.append(9)
dll.append(14)
dll.append(20)

print("Doubly Linked List:")
dll.display()
key = 9
if dll.search(key):
    print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")
