"""
A tree class created for 
Depth First Search practice

@author: Ms. Namasivayam
@version: ATCS 2023-2024
"""
from node import Node

SMALL = "sm"
MEDIUM = "md"

class Tree:
    def __init__(self, root=None, generate=None):
        if root:
            self.root = root
        elif generate == SMALL:
            self.generate_small()
        else:
            self.generate_medium()
    
    def add_child(self, parent, value):
        child = Node(value, parent)
        parent.add_child(child)
        return child

    def generate_small(self):
        """
        Generates a small tree with 3 
        levels and 8 total nodes
        """
        # Small tree with 3 levels and 6 nodes
        self.root = Node(5)

        # Level 1
        level1_child1 = self.add_child(self.root, 1)
        level1_child2 = self.add_child(self.root, 3)
        level1_child3 = self.add_child(self.root, 2)

        # Level 2
        level2_child1 = self.add_child(level1_child1, 7)
        level2_child2 = self.add_child(level1_child2, 4)
        level2_child3 = self.add_child(level1_child2, 12)
        level2_child4 = self.add_child(level1_child2, 6)
    
    def generate_medium(self):
        """
        Generates a medium tree with 3 
        levels and 16 total nodes
        """
        self.root = Node(1)

        # Level 1
        level1_child1 = self.add_child(self.root, 2)
        level1_child2 = self.add_child(self.root, 9)
        level1_child3 = self.add_child(self.root, 10)

        # Level 2
        level2_child1 = self.add_child(level1_child1, 3)
        level2_child2 = self.add_child(level1_child1, 4)
        level2_child3 = self.add_child(level1_child1, 8)
        level2_child4 = self.add_child(level1_child3, 11)
        level2_child5 = self.add_child(level1_child3, 12)

        # Level 3
        level3_child1 = self.add_child(level2_child2, 5)
        level3_child2 = self.add_child(level2_child2, 6)
        level3_child3 = self.add_child(level2_child2, 7)
        level3_child4 = self.add_child(level2_child5, 13)
        level3_child5 = self.add_child(level2_child5, 14)
        level3_child6 = self.add_child(level2_child5, 15)
        level3_child7 = self.add_child(level2_child5, 16)
    


    def do_dfs(self, node):
        if node.is_leaf():
            print(node)
            return 
        else:
            print(node)
        for child in range(len(node.children)):
            self.do_dfs(node.children[child])


    def dfs_printer(self):
        # TODO: Use recursion to print the 
        # order the nodes would be visited 
        # when using DFS
        self.do_dfs(self.root)
        pass

    
    def find_val(self, node, value):
        if node.value == value:
            return True
        is_found = False
        for child in range(len(node.children)):
            is_found = is_found or self.find_val(node.children[child], value)
        
        return is_found


    def dfs(self, value):
        # TODO: Use recursion to find the 
        # value in the current tree
        # return True if found and False otherwise
        return self.find_val(self.root, value)


        





if __name__ == "__main__":
    t = Tree(generate=MEDIUM)
    # Should print numbers in order
    #t.dfs_printer()

    t = Tree(generate=SMALL)
    # Should return True
    #print(t.dfs(12))

    # Should return False
    #print(t.dfs(10))    