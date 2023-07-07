from Node import Node
from BST import BST

class LinkedList:
    
    def __init__(self, head_node_value):
        self.head = Node(head_node_value)
    
    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.right
        return  f'<LinkedList: {" -> ".join(nodes)}>'
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right
        
    def append_node(self, value):
        new_node = Node(value)
        for node in self:
            pass
        node.right = new_node
        # current_node = self.head
        # while current_node.right:
        #     current_node = current_node.right
        # current_node.right = new_node
    
    def insert_node(self, value, prev_node_value):
        new_node = Node(value)
        for node in self:
            if node.value == prev_node_value:
                new_node.right = node.right
                node.right = new_node
                return
        print(f'{prev_node_value = } not valid')
    
    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right and node.right.value == value:
                    node.right = node.right.right
                    return
            print(f'Value: {value} not found')
            
    def remove_tail(self):
        for node in self:
            pass
        self.remove_node(node.value)
    
    def get_tail(self):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    # Christian's solution
        # for node in self:
        #     if not node.right:
        #       self.tail = node
        #       print(f'LinkedList tail: {self.tail}')
    
    def print_list(self):
        nodes = []
        for node in self:
            nodes.append(str(node.value))
        print(" -> ".join(nodes))
    
"""
make method 
takes in a list
turns list into bst
whit bst create a sorted linked list
"""
def create_sorted_linked_list(self, alist):
    bst = BST(alist[0])
    for i, e in enumerate(alist):
        if i != 0:
            bst.add_node(e)
    bst.storing_sorted_values()
    self.head = Node(bst.sorted_node_values[0])
    for i, num in enumerate(bst.sorted_node_values):
        if i != 0:
            self.append_node(num)

    
linked_list = LinkedList(None)
linked_list.create_sorted_linked_list([19,1,5,3,10])
print(linked_list)

    
# linked_list = LinkedList('monday')
# linked_list.append_node('tuesday')
# linked_list.append_node('wednesday')
# linked_list.append_node('friday')

# # print(linked_list.head)
# # print(linked_list.head.right)
# # print(linked_list.head.right.right)
# print(linked_list)

# linked_list.insert_node('thursday', 'wednesday')
# # linked_list.insert_node('sunday', 'saturday')
# linked_list.remove_tail()

# #needs __iter__method
# for n in linked_list:
#     print(n)

# linked_list.remove_node('saturday')
# print(linked_list.get_tail())
# print(linked_list.print_list())

# print([node for node in linked_list])