from Node import Node

class BST:
    
    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)
        self.sorted_node_values = []
        
    def add_node(self, value, node=None):
        new_node = Node(value)
        if not node:
            node = self.head_node
        if value > node.value:
            if not node.right:
                node.right = new_node
            else:
                self.add_node(value, node.right)
        elif value < node.value:
            if not node.left:
                node.left = new_node
            else:
                self.add_node(value, node.left)
    
    def get_min(self, node=None):
        if not node:
            node = self.head_node
        if node.left:
            return self.get_min(node.left) #recursively call method to continue looking to the left until it cannot any further
        else:
            return node
    
    def get_max(self, node=None):
        if not node:
            node = self.head_node
        if node.right:
            return self.get_max(node.right)
        else:
            return node
    
    def search_node(self, target_value, node=None):
        if not node:
            node = self.head_node
        if target_value == node.value:
            return True
        elif target_value > node.value:
            return self.search_node(target_value, node.right) if node.right else False
            # if node.right:
            #     return self.search_node(target_value, node.right)
            # else:
            #     return False
        return self.search_node(target_value, node.left) if node.left else False
    
    def print_in_order(self, node = None):
        if not node:
            node = self.head_node
        if node.left:
            self.print_in_order(node.left)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)

    def storing_sorted_values(self, node = None):
        if not node:
            node = self.head_node
        if node.left:
            self.storing_sorted_values(node.left)
        self.sorted_node_values.append(node.value)
        if node.right:
            self.storing_sorted_values(node.right)
        
if __name__ == '__main__':    
    bst = BST(100)

# print(bst)

# bst.add_node(105)
# bst.add_node(130)
# bst.add_node(115)

# bst.add_node(75)
# bst.add_node(50)
# bst.add_node(60)
# bst.add_node(40)

# print(bst.head_node.right.right.left)
# print(bst.head_node.left.left.right)
# print(bst.head_node.right.right.left)

# print(bst.get_min())
# print(bst.get_max())

# print(bst.search_node(75))
# print(bst.search_node(50))
# print(bst.search_node(115))
# print(bst.search_node(17))
# print(bst.search_node(117))

# print(bst.print_in_order())