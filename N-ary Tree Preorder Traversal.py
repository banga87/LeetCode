"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value
"""
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def preorder(root: Node) -> list[int]:
    if root == None:
        return []
    
    stack = [root]
    output = []

    while stack:
        current_node = stack.pop() # takes from the right side
        output.append(current_node.val)
        stack.extend(current_node.children[::-1]) # reverses order of list and appends to the right side.

    print(output)


    
grandma = Node('Grandma')
dad = Node('Dad')
son = Node('Son')
daughter = Node('Daughter')
grandson = Node("Son's Son")
grandaughter = Node("Son's Daughter")

grandma.add_child(dad)
dad.add_child(son)
dad.add_child(daughter)
son.add_child(grandson)
son.add_child(grandaughter)

preorder(grandma)


