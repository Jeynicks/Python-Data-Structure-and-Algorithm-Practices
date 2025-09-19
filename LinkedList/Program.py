from LinkedList import LinkedList

def display_node(linked_list):
    current = linked_list.head
    elements = []
    
    while current:
        elements.append(str(current.value))
        current = current.next

    print(' <-> '.join(elements))


linkedlist = LinkedList()

print('\nAppend 36 to our Linked List')
linkedlist.append(36)
display_node(linkedlist)

print('\nExtend [67, 69] to our Linked List')
linkedlist.extend([67, 69])
display_node(linkedlist)

print('\nInsert 8 in index 1 to our Linked List')
linkedlist.insert(1, 8)
display_node(linkedlist)

print('\nInsert iterable [22, 24] in index 0 to our Linked List')
linkedlist.insert_iter(0, [22, 24])
display_node(linkedlist)

print('\nRemove 67 to our Linked List')
linkedlist.remove(67)
display_node(linkedlist)

print('\nPop index 3 to our Linked List')
pop = linkedlist.pop(3)
print('Pop: ' + str(pop))
display_node(linkedlist)

print('\nClear our Linked List')
linkedlist.clear()
display_node(linkedlist)
   