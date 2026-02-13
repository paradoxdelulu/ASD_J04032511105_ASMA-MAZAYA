#=====================================================================
# Latihan 1 :
# Implementasikan fungsi untuk menghapus node dengan nilai tertentu.	
#=====================================================================

class node:
    def	__init__(self, data):	
        self.data = data	
        self.next = None

class linked_list:
    def	__init__(self):	
        self.head =	None

    def append(self, new_data):    
        new_node = node(new_data)	
        if self.head is None:	
            self.head = new_node	
            return	
        last = self.head	
        while last.next:	
            last = last.next	
        last.next = new_node

    def delete_node(self, key):	
        temp = self.head	
        if temp and temp.data == key:	
            self.head = temp.next	
            temp = None	
            return	        
        prev = None	
        while temp and temp.data != key:	
            prev = temp	
            temp = temp.next	
        if temp is None:	
            return
        prev.next = temp.next	
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ========== TEST ==========
ll = linked_list()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Sebelum dihapus:")
ll.display()
ll.delete_node(20)

print("Setelah dihapus:")
ll.display()
