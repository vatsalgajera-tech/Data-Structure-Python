from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,root,data):
        if root == None:
            return TreeNode(data)
        if data > root.data:
            root.right = self.insert(root.right,data)
        else:
            root.left = self.insert(root.left,data)
        return root

    def preorder(self,root):
        if root:
            print(root.data,end=" -> ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" -> ")
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" -> ")
            self.inorder(root.right)
            
    def bfs_traversal(self,root):
        if root is None:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            print(node.data,end=" -> ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
    def findMin(self,root):
        if root is None:
            return None
        curr = root
        while curr.left:
            curr = curr.left
        print(curr.data)
        
    def findMax(self,root):
        if root is None:
            return None
        curr = root
        while curr.right:
            curr = curr.right
        print(curr.data)
            
    def heightOfTree(self,root):
        if root is None:
            return 0
        return 1 + max(self.heightOfTree(root.left),self.heightOfTree(root.right))
            
    def countNodes(self,root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def search(self, root, key):
        if root is None:
            return None
        if root.data == key:
            return root.data
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
            
    def deleteNode(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.findMin(root.right)
            root.data = temp.data
            root.right = self.deleteNode(root.right, temp.data)
        return root
    
bst = BinarySearchTree()
bst.root = bst.insert(bst.root,50)
bst.insert(bst.root, 10)
bst.insert(bst.root, 30)
bst.insert(bst.root, 0)
bst.insert(bst.root, 70)
print("Preorder Traversal :")
bst.preorder(bst.root)
print("\nPostorder Traversal :")
bst.postorder(bst.root)
print("\nInorder Traversal :")
bst.inorder(bst.root)
print("\nBreadth First Travesal : ")
bst.bfs_traversal(bst.root)
print("\nMinimum Value : ",end="")
bst.findMin(bst.root)
print("Maximum Value : ",end="")
bst.findMax(bst.root)
print("Height of Tree : ",end="")
print(bst.heightOfTree(bst.root))
print("Count Nodes : ",end="")
print(bst.countNodes(bst.root))
print("Search Node : ",end="")
print(bst.search(bst.root,30))
print("Delete Node : ",end="")
bst.deleteNode(bst.root,30)
bst.inorder(bst.root)