from linked_list import LinkedList, Node

linkedlist = LinkedList()

linkedlist.add(5)
linkedlist.add(4)
linkedlist.add(3)
linkedlist.add(2)
linkedlist.add(1)
linkedlist.add(0)

def middle_of_linked_list(head: Node) -> int: 
    slow = fast = head
    if head == None: 
        return None 
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node
    return slow.data
    
if __name__ == '__main__':  
    print(middle_of_linked_list(linkedlist.head))