class Avlnode:
    __slots__ = ['item','left','right','height']
    def __init__(self,item,left = None,right = None,height = 1):
        """
        Initialize a new Avlnode object.
        
        Parameters:
        - item: The value/item stored in the node.
        - left: The left child node (default: None).
        - right: The right child node (default: None).
        - height: The height of the node (default: 1).
        """
        self.item = item
        self.left = left
        self.right = right
        self.height = height

class AVLTree:
    def __init__(self):
        self.root = None
        
    def get_height(self, pos):
        """
        Return the height of a given node.
        
        Parameters:
        - pos: The node to calculate the height.
        
        Returns:
        - The height of the node if it exists, otherwise 0.
        """
        if pos is None:
            return 0
        return pos.height
    
    def get_balance_factor(self, pos):
        """
        Return the balance factor of a given node.
        
        Parameters:
        - pos: The node to calculate the balance factor.
        
        Returns:
        - The balance factor of the node if it exists, otherwise 0.
        """
        if pos is None:
            return 0
        return self.get_height(pos.left) - self.get_height(pos.right)

    def insert(self, item):
        """
        Insert a new item into the AVL tree.
        
        Parameters:
        - item: The item to be inserted.
        """
        self.root = self._insert(self.root, item)

    def _insert(self, pos, item):
        """
        Helper function to insert a new item into the AVL tree.
        
        Parameters:
        - pos: The current node being checked.
        - item: The item to be inserted.
        
        Returns:
        - The updated node after insertion.
        """
        if pos is None :
            return Avlnode(item)
        elif item < pos.item:
            pos.left = self._insert(pos.left, item)
        else:
            pos.right = self._insert(pos.right, item)

        pos.height = 1 + max(self.get_height(pos.left), self.get_height(pos.right))

        balance_factor = self.get_balance_factor(pos)

        # Perform appropriate rotations based on the balance factor
        if balance_factor > 1:
            if item < pos.left.item:
                return self.rotate_right(pos)
            else:
                pos.left = self.rotate_left(pos.left)
                return self.rotate_right(pos)
        if balance_factor < -1:
            if item > pos.right.item:
                return self.rotate_left(pos)
            else:
                pos.right = self.rotate_right(pos.right)
                return self.rotate_left(pos)

        return pos

    def rotate_left(self, pos):
        """
        Perform a left rotation on a given node.
        
        Parameters:
        - pos: The node to perform the left rotation.
        
        Returns:
        - The updated node after the left rotation.
        """
        y = pos.right
        z = y.left

        y.left = pos
        pos.right = z

        pos.height = 1 + max(self.get_height(pos.left), self.get_height(pos.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, pos):
        """
        Perform a right rotation on a given node.
        
        Parameters:
        - pos: The node to perform the right rotation.
        
        Returns:
        - The updated node after the right rotation.
        """
        y = pos.left
        z = y.right

        y.right = pos
        pos.left = z

        pos.height = 1 + max(self.get_height(pos.left), self.get_height(pos.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def preorder(self, pos):
        """
        Perform a pre-order traversal of the AVL tree.
        
        Parameters:
        - pos: The starting node for traversal.
        
        Returns:
        - A string representation of the pre-order traversal.
        """
        res = f"[{pos.item}"
        if pos.left is not None:
            res += self.preorder(pos.left)
        if pos.right is not None:
            res += self.preorder(pos.right)
        res += "]"
        return res

    def __str__(self):
        """
        Return a string representation of the AVL tree.
        """
        if self.root is not None:
            return self.preorder(self.root)
        else:
            raise ValueError("the tree is empty")


# Usage example
tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)
print("Pre-order traversal of the AVL tree:")
print(tree)
print("--------------------------------------------------------")
tree1 = AVLTree()
tree1.insert(1)
tree1.insert(2)
tree1.insert(3)
tree1.insert(4)
print("Pre-order traversal of the AVL tree:")
print(tree1)
print("--------------------------------------------------------")
tree2 = AVLTree()
tree2.insert(0)
tree2.insert(1)
tree2.insert(99)
print("Pre-order traversal of the AVL tree:")
print(tree2)
print("--------------------------------------------------------")
tree3 = AVLTree()
tree3.insert(1)
tree3.insert(9999)
tree3.insert(99)
tree3.insert(999)
tree3.insert(9)
print("Pre-order traversal of the AVL tree:")
print(tree3)
print("--------------------------------------------------------")
tree5 = AVLTree()
print("Pre-order traversal of the AVL tree:")
print(tree5)
