class Node:
    def __init__(self, data):
        self.data = data #asigna el valor del nodo
        self.next = None #Inicializa el atrivuto 'next' como null

class LinkedList:
    def __init__(self):
        self.head = None #inicializa la cabeza de la lista como null
    
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next 
        print()
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return 'The list is empty'
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if self.head is None:
            return 'The list is empty'
        if self.head.next is None:
            self.haed = None 
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, value):
        current = self.head
        position = 0 
        while current:
            if current.data == value:
                return f"Value '{value}' found at position {position}"
            current = current.next
            position +=1
        return f"Value '{value}' not found in the list"
    

    def deleteDuplicate(self):
        if not self.head:
            return 
        node = self.head
        while node.next:
            if node.data == node.next.data:
                node.next = node.next.next
            else:
                node = node.next
        


if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtBeginning('fox')
    llist.insertAtBeginning('brown')
    llist.insertAtBeginning('quick')
    llist.insertAtBeginning('the')

    llist.printList()

    llist.insertAtEnd('jumps')

    llist.printList()
    
    
    # Deleting nodes from the beginning and end
    llist.deleteFromBeginning()
    llist.deleteFromEnd()

    # Print the list after deletion
    print("List after deletion:")
    llist.printList()

        # Search for 'quick' and 'lazy' in the list
    print(llist.search('quick'))  # Expected to find
    print(llist.search('lazy'))   # Expected not to find


    llist2 =  LinkedList()
    llist2.insertAtEnd(1)
    llist2.insertAtEnd(1)
    llist2.insertAtEnd(2)
    llist2.insertAtEnd(3)
    llist2.insertAtEnd(4)
    llist2.insertAtEnd(4)
    llist2.insertAtEnd(5)
    llist2.printList()
    llist2.deleteDuplicate()
    llist2.printList()

   