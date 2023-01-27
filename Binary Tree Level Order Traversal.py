from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    queue = deque()
    queue.append(root)
    output = []

    while queue:
        length = len(queue)
        level = []
        # This will iterate over nodes in the queue based on the size of the queue when it begins iterating.
        for i in range(length):
            node = queue.popleft()
            if node:
                # Adding nodes to the end of the queue.
                # These nodes will be iterated over during the next pass
                # of the while loop
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            output.append(level)
    
    return output

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.left = two
one.right = three
two.left = four
three.right = five

print(levelOrder(one))