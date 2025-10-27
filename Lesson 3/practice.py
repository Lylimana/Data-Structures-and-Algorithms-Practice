from linked_list import Node, LinkedList

N1 = Node(10)

N2 = Node(20)

N1.next_node = N2

print(N1.next_node)

linkedlist = LinkedList()

linkedlist.head = N1 

linkedlist.add(30)
linkedlist.add(40)
linkedlist.add(50)
linkedlist.add(60)

print(linkedlist.size())

linkedlist
# Output: [Head: 60]-> [50]-> [40]-> [30]-> [10]-> [Tail: 20]

print(linkedlist.search(40))