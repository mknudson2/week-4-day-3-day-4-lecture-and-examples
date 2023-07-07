from Node import Node

class BST:
    
    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)

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
            return self.get_min(node.left)
        else:
            return node
        
    def get_max(self, node = None):
        if not node:
            node = self.head_node
        if node.right:
            return self.get_max(node.right)
        else:
            return node
    
    def search_node(self, node_value):
        pass
    

bst = BST(100)

print(bst)

bst.add_node(105)
bst.add_node(130)
bst.add_node(115)

bst.add_node(75)
bst.add_node(50)
bst.add_node(60)



print(bst.head_node.right.right.left)
print(bst.head_node.left, 75)
print(bst.head_node.left.left, 50)
print(bst.head_node.left.left.right, 60)
bst.add_node(40)

print(bst.get_min())
print(bst.get_max())