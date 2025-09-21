from LinkedList import LinkedList

def display_node(linked_list):
    current = linked_list.head
    elements = []
    
    while current:
        elements.append(str(current.value))
        current = current.next

    print(' <-> '.join(elements))


linkedlist = LinkedList()
linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

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

print('\nConvert Iterable [1, 2, 3, 4, 5] into a Linked List1')
linkedlist1.convert([1, 2, 3, 4, 5])
display_node(linkedlist1)

print('\nMerge our Linked List1 to Linked List')
linkedlist.merge(linkedlist1)
display_node(linkedlist)    

print('\nCopy our Linked List to Linked List 2')
linkedlist2 = linkedlist.copy()
display_node(linkedlist2)
 
print('\nLinked List 2 as Iterable')    
for linked_list in linkedlist2:
    print(f"{linked_list}, ", end=" ")


print('\n\nFind 36 ')
display_node(linkedlist2)
print('Index: '+str(linkedlist2.find(36)))

print('\nGet Value of Index 5')
display_node(linkedlist2)
print('Value: '+str(linkedlist2.get(5)))

print('\nSet Value of Index 5 to 30')
linkedlist2.set(5, 30)
display_node(linkedlist2)

print('\nLinkedList is now subscriptable')
print(linkedlist2[3])   
