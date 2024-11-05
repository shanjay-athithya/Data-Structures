from abstractbinarytree import AbstractBinaryTree
class BinaryTree(AbstractBinaryTree):
    """
    BinaryTree is a concrete implementation of AbstractBinaryTree that represents a binary tree.
    It uses the BTNode class to create nodes of the tree.
    """
    class BTNode:
        """
        BTNode is a nested class that represents a node in the binary tree.
        """
        __slots__ = ['item','left','right','parent']
        def __init__(self, item, left = None, right = None, parent = None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def getitem(self):
            """
            Returns the item stored in the node.

            Returns:
                The item stored in the node.
            """
            return self.item

        def setitem(self, item):
            """
            Sets the item of the node to the specified item.

            Args:
                item: The item to be set.
            """
            self.item = item

    def __init__(self, item, Tleft = None, Tright = None, parent = None):
        """
        Initializes a BinaryTree.

        Args:
            item: The item to be added as the root of the tree.
            Tleft: The left subtree of the tree.
            Tright: The right subtree of the tree.
            parent: The parent node of the tree.
        """
        self.root = None
        self.size = 0
        if item is not None:
            self.root = self.addroot(item)
        if Tleft is not None:
            if Tleft.root is not None:
                Tleft.root.parent = self.root
                self.root.left = Tleft.root
                self.size += Tleft.size
                Tleft.root = None
                Tleft.size = 0
        if Tright is not None:
            if Tright.root is not None:
                Tright.root.parent = self.root
                self.root.right = Tright.root
                self.size += Tright.size
                Tright.root = None
                Tright.size = 0
                    
    def addroot(self, item):
        """
        Adds a root node with the specified item to the tree.

        Args:
            item: The item to be added as the root.

        Returns:
            The newly added root node.
        """
        if self.root is None:
            self.root = self.BTNode(item)
            self.size = 1
            return self.root
        else:
            raise ValueError("root is already present")
    
    def __len__(self):
        """
        Returns the total number of nodes in the tree.

        Returns:
            The number of nodes in the tree.
        """
        return self.size
    
    def getleft(self, pos):
        """
        Returns the position of the left child node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the left child node.
        """
        return self.left(pos)

    def getright(self,pos):
        """
        Returns the position of the right child node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the right child node.
        """
        return self.right(pos)
    
    def getroot(self):
        """
        Returns the position of the root node of the tree.

        Returns:
            The position of the root node.
        """
        return self.root
    
    def addleft(self, item, pos):
        """
        Adds a left child node with the specified item to the given position.

        Args:
            item: The item to be added.
            pos: The position to which the left child node should be added.

        Raises:
            ValueError: If the position already has a left child node.
        """
        if self.getleft(pos) is None:
            pos.left = self.BTNode(item, parent = pos)
            self.size += 1
        else:
            raise ValueError('already a left element exists')

    def addright(self, item, pos):
        """
        Adds a right child node with the specified item to the given position.

        Args:
            item: The item to be added.
            pos: The position to which the right child node should be added.

        Raises:
            ValueError: If the position already has a right child node.
        """
        if self.getright(pos) is None:
            pos.right = self.BTNode(item, parent = pos)
            self.size += 1
        else:
            raise ValueError('already a right element exists')

    def preorder(self, pos):
        """
        Performs a preorder traversal of the tree starting from the specified position.

        Args:
            pos: The position from which the traversal should start.
        """
        res=f"[{pos.item}"
        if pos.left is not None:
            res+=self.preorder(pos.left)
        if pos.right is not None:
            res+=self.preorder(pos.right)
        res+="]"
        return res
    
    def inorder(self, pos):
        """
        Performs an inorder traversal of the tree starting from the specified position.

        Args:
            pos: The position from which the traversal should start.
        """
        res = ''
        if pos.left is not None:
            res += self.inorder(pos.left)
        res += f"[{pos.item}"
        if pos.right is not None:
            res += self.inorder(pos.right)
        res += ']'
        return res
    
    def postorder(self, pos):
        """
        Performs a postorder traversal of the tree starting from the specified position.

        Args:
            pos: The position from which the traversal should start.
        """
        res = ''
        if pos.left is not None:
            res += self.postorder(pos.left)
        if pos.right is not None:
            res += self.postorder(pos.right)
        res = f"[{pos.item}]" + res
        return res
            
    def mirror(self, pos):
        if pos is not None:
            pos.left, pos.right = pos.right, pos.left
            self.mirror(pos.left)
            self.mirror(pos.right)
            
    
    def __str__(self):
        """
        Returns a string representation of the tree.

        Returns:
            A string representation of the tree.
        """
        return self.preorder(self.root)
    
if __name__ == '__main__':
    tree = BinaryTree(0)
    tree.addleft(10, tree.root)
    tree.addright(20, tree.root)
    tree.addleft(30, tree.root.left)
    tree.addright(40, tree.root.left)
    tree.addleft(50, tree.root.right)
    print("the original tree")
    print(tree)
    tree.mirror(tree.root)
    print("the mirror tree")
    print(tree)
    print("the post order tree")
    print(tree.postorder(tree.root))
    print("the inorder tree")
    print(tree.inorder(tree.root))