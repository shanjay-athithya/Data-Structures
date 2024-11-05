from binarytree import BinaryTree

#class BinarySearchTree(BinaryTree):
class BinarySearchTree(BinaryTree):
    def __init__(self, item = None, tleft = None, tright = None):
        super().__init__( item, tleft, tright)
    def construct(self, item, pos):
        if pos is None:
            self.root = self.addroot(item)
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
        elif pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos.item
    def findmax(self, pos):
        if pos is None:
            return pos
        elif pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos.item
    def delete(self, item):
        pos = self.search(self.root, item)
        parent = pos.parent
        if pos.left is None and pos.right is None:
            if pos is parent.right:
                parent.right = None
            elif pos is parent.left:
                parent.left = None
        if pos.left is not None and pos.right is None:
            parent.left = pos.left
        elif pos.right is not None and pos.left is None:
            parent.right = pos.right
        else:  # When the node has both left and right children
            inorder_successor = self.findmin(pos.right)
            pos.item = inorder_successor
            self.delete(inorder_successor, pos.right)

            
            
    
            
if __name__ == '__main__':
    bst = BinarySearchTree(5)
    bst.construct(10, bst.getroot())
    bst.construct(4, bst.getroot())
    bst.construct(1, bst.root)
    bst.construct(7, bst.root)
    print("the binary search tree is")
    print(bst)
    print("----------------------------------------------------")
    
    print("the max element is :")
    print(bst.findmax(bst.root))
    print("----------------------------------------------------")
    
    print("the min element is :")
    print(bst.findmin(bst.root))
    print("----------------------------------------------------")
    
    bst.delete(4)
    print("the tree after deteting '4' :")
    print(bst)
    print("----------------------------------------------------")
    
    b1 = BinarySearchTree()
    b1.construct(1, b1.getroot())
    b1.construct(111, b1.getroot())
    b1.construct(1111,b1.root)
    b1.construct(2, b1.root)
    print("the binary search tree is")
    print(b1)
    
    