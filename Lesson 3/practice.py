from linked_list import Node, LinkedList

N1 = Node(10)

linkedlist = LinkedList()

linkedlist.head = N1

linkedlist.add(20)
linkedlist.add(30)
linkedlist.add(40)
linkedlist.add(50)
linkedlist.add(60)

print(linkedlist.size())

linkedlist
# Output: [Head: 60]-> [50]-> [40]-> [30]-> [10]-> [Tail: 20]

print(linkedlist.search(40))
# <Node data: 40>

print(linkedlist.insert(35, 3))
# [Head: 60]-> [50]-> [40]-> [35]-> [30]-> [20]-> [Tail: 10]

print(linkedlist.remove(35))

linkedlist.remove_index(5)

print(linkedlist)

