class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end=sep)
        node = node.next
    print()
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    # sorted_merged_list = []
    sorted_merged_linked_lists = SinglyLinkedList()
    
    while head1 or head2:
        
        if head1 and head2:
            if head1.data == head2.data:
                # sorted_merged_list.extend([head1.data, head2.data])
                sorted_merged_linked_lists.insert_node(head1.data)
                sorted_merged_linked_lists.insert_node(head2.data)
                head1 = head1.next
                head2 = head2.next
                
            elif head1.data < head2.data:
                # sorted_merged_list.append(head1.data)
                sorted_merged_linked_lists.insert_node(head1.data)
                head1 = head1.next
                
            else:
                # sorted_merged_list.append(head2.data)
                sorted_merged_linked_lists.insert_node(head2.data)
                head2 = head2.next
            
        else:
            # sorted_merged_list.append(head1.data if head2 is None else head2.data)
            sorted_merged_linked_lists.insert_node(head1.data if head2 is None else head2.data)
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

    # print(sorted_merged_list)
    # print(sorted_merged_linked_lists.head.data)
    
    return sorted_merged_linked_lists.head


l1 = [1,2,3] 
l2 = [2,3,4] # 1 2 3 3 4 

l1 = [4,5,6] 
l2 = [1,2,10] # 1 2 4 5 6 10 

l1 = [8,11,17,20,20,42,83,94,95]
l2 = [1] # 1 8 11 17 20 20 42 83 94 95 

llist1 = SinglyLinkedList()
for i in l1:
    llist1.insert_node(i)
    

llist2 = SinglyLinkedList()
for i in l2:
    llist2.insert_node(i)

print_singly_linked_list(mergeLists(llist1.head,llist2.head), ",")