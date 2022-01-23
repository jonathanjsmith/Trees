"""
https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.
"""

class Node:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def nearestRight(root, u):
    
    # use BFS to find next right node
    q = [(root, 0)]
    while q:
        node, level = q.pop(0)
        if node == u:
            if q and level == q[0][1]:
                return q[0][0]
            return None
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
            
"""
Time: O(n)
Space: O(D) where D is diameter of tree
"""

input_1 = Node(1)
input_1.left = Node(2)
input_1.right = Node(3)
input_1.left.right = u = Node(4)
input_1.right.left = Node(5)
input_1.right.right = Node(6)

ans = nearestRight(input_1, u)
print(ans.val)