from linked_list import Node, LinkedList
from linked_list_merge_sort import merge_sort

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

linkedlist1 = LinkedList()

linkedlist1.add(2)
linkedlist1.add(24)
linkedlist1.add(46)
linkedlist1.add(68)
linkedlist1.add(81)
linkedlist1.add(1)
linkedlist1.add(35)
linkedlist1.add(57)
linkedlist1.add(79)
linkedlist1.add(92)

print(linkedlist1)

print(merge_sort(linkedlist1))
