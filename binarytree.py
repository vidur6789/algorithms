from cmath import inf
from collections import deque
from tkinter.tix import Tree


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    
    def _dfs_helper(self, node, path=[]):
        if node == None:
            return
        if node.left:
           self._dfs_helper(node.left, path)
        print(node.value)
        path.append(node.value)
        if node.right:
            self._dfs_helper(node.right, path)
        return path
        
    

    def depth_first_search(self):
        return self._dfs_helper(self)


    def breadth_first_search(self):
        path = []
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            cur_node = queue.popleft()
            print(cur_node.value)
            path.append(cur_node.value)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return path


        

'''
tree = Node(
    value='a', 
    left=Node(
        value='b',
        left=Node('d')), 
    right=Node(
        value='c',
        right=Node(
            value='e',
            left=Node(
                value='f',
                left=Node('g'),
                right=Node('h')
            )
        )
    )
)
'''


tree = Node(
    value=1,
    left=Node(
        value=2,
        left=Node(4),
        right=Node(5)
    ),
    right=Node(
        value=3,
        left=Node(6),
        right=Node(7))
)




def tree_contains(tree, target):
    if not tree or not target:
        return False
    elif tree.value == target:
        return True
    return tree_contains(tree.left, target) \
        or tree_contains(tree.right, target)





def tree_sum(tree):
    if not tree:
        return 0
    
    return tree_sum(tree.left) + tree.value + tree_sum(tree.right)


def tree_min(tree):
    if not tree:
        return inf
    
    return min(tree_min(tree.left), tree.value, tree_min(tree.right))


def max_root_leaf_sum(tree, sum=0):
    if not tree:
        return sum
    sum += tree.value
    print(sum, tree.value)
    return max(max_root_leaf_sum(tree.left, sum), max_root_leaf_sum(tree.right, sum))


def max_root_leaf_sum_alt(tree):
    if not tree:
        return -inf
    
    print(tree.value)
    return max(
        tree.value + max_root_leaf_sum(tree.left), 
        tree.value + max_root_leaf_sum(tree.right)
        )


    

print(tree.depth_first_search())
print(tree.breadth_first_search())
print(tree_contains(tree, 7))
print(tree_sum(tree))
print(tree_min(tree))
print(max_root_leaf_sum(tree))
print(max_root_leaf_sum_alt(tree))
