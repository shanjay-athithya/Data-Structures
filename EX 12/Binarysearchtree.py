from binarysearchtree.py import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def __init__(self, item = None, lchild = None, rchild = None):
        super().__init__(item, lchild, rchild)
        
    def construct(self, item, pos):
        if pos is None:
            self.addroot(item)
        elif item < pos.item:
            if pos.left is None:
                self.addleft(item, pos)
            else:
                self.construct(item, pos.left)
        elif item > pos.item:
            if pos.right is None:
                self.addright(item, pos)
            else:
                self.construct(item, pos.right)
    
    def search(self, pos, item):
        if pos is None:
            return pos
        if item < pos.item:
            return self.search(pos.left, item)
        if item > pos.item:
            return self.search(pos.right, item)    
        if item == pos.item:
            return pos
        
    def findmin(self, pos):
        if pos is None:
            return pos
        if pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos.item
    
    def findmax(self, pos):
        if pos is None:
            return None
        if pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos.item
        
    def delete(self, item): 
        pos = self.search(self.root,item)
        parent = pos.parent
        if pos.right is None and pos.left is not None:
            if pos == parent.right:
                parent.right = None
            elif pos == parent.left:
                parent.left = None
        elif pos.right is not None and pos.left is None:
            parent.right = pos.right
            pos.parent = pos.left = pos.right = None
        elif pos.left is not None and pos.right is None:
            parent.left = pos.left
            pos.parent = pos.right = pos.left = None
            
        elif pos.right is not None and pos.left is not None:
            inorder_successor=self.findmin(pos.right)
            pos.item=inorder_successor.item
            parent=inorder_successor.parent
            parent.right =None
            return
            
if __name__ == '__main__':
    bst = BinarySearchTree(5)
    bst.construct(10, bst.getroot())
    bst.construct(11, bst.getroot())
    bst.construct(1, bst.root)
    bst.construct(2, bst.root)
    print("the binary search tree is")
    print(bst)
    print("----------------------------------------------------")
    
    print("the max element is :")
    print(bst.findmax(bst.root))
    print("----------------------------------------------------")
    
    print("the min element is :")
    print(bst.findmin(bst.root))
    print("----------------------------------------------------")
    
    bst.delete(10)
    print("the tree after deteting '10' :")
    print(bst)
    print("----------------------------------------------------")
    
    b1 = BinarySearchTree()
    b1.construct(1, b1.getroot())
    b1.construct(111, b1.getroot())
    b1.construct(1111,b1.root)
    b1.construct(2, b1.root)
    print("the binary search tree is")
    print(b1)
    
    