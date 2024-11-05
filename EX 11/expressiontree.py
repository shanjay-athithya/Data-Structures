from binarytree import BinaryTree
class ExpressionTree(BinaryTree):
    """
    ExpressionTree is a subclass of BinaryTree that represents an expression tree.
    It provides methods to create an expression tree from a postfix string and perform a postorder traversal.
    """
    def __init__(self, item = None, tleft = None, tright = None):
        """
        Initializes an ExpressionTree.

        Args:
            item: The item to be added as the root of the tree.
            tleft: The left subtree of the tree.
            tright: The right subtree of the tree.
        """
        super().__init__(item, tleft, tright)
    def create(self, string):
        
        """
        Creates an expression tree from a postfix string.

        Args:
            string: The postfix string representing the expression.

        Returns:
            The root position of the created expression tree.
        """
        stack = []
        for ch in string:
            if ch in ['+', '-', '*','/']:
                rchild = stack.pop()
                lchild = stack.pop()
                stack.append(ExpressionTree(ch, lchild, rchild))
            else:
                stack.append(ExpressionTree(ch))
        self.root = stack.pop().getroot()
        return self.root

if __name__ == '__main__':
    tree = ExpressionTree()
    tree.create('ab+a*cd-e+/afg-*h+-') #ab-c/f*d+
    print(tree)