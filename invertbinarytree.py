"""
https://leetcode.com/problems/invert-binary-tree/submissions/
Given the root of a binary tree, invert the tree, and return its root.
"""

class Node:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def invertV1(root):
    # recursive approach
    if root:
        root.left, root.right = invertV1(root.right), invertV2(root.left)
    return root

"""
Time: O(n)
Space: O(h)
"""

def invertV2(root):
    # iterative approach using queue BFS
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root

"""
Time: O(n)
Space: O(n)
"""

input_1 = Node(4)
input_1.left = Node(2)
input_1.right = Node(7)
input_1.left.left = Node(1)
input_1.left.right = Node(3)
input_1.right.left = Node(6)
input_1.right.right = Node(9)

def printTree(root):
    h = 0
    q = [(root, 0)]
    print("[0] -> ", end='')
    while q:
        node, height = q.pop(0)
        if height > h:
            h += 1
            print("\n[" + str(h) + "] -> ", end = '')
        print(node.val, end=' ')
        if node.left:
            q.append((node.left, height+1))
        if node.right:
            q.append((node.right, height+1))
    print()
        
ans1 = invertV1(input_1)
printTree(ans1)
print()
ans2 = invertV2(input_1)
printTree(ans2)
