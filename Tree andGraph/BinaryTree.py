from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def level_order(self):
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bt = BinaryTree()
elements = [10, 20, 30, 40, 50, 60, 70]

for el in elements:
    bt.insert(el)

print("Level Order:")
bt.level_order()
