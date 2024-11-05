from abstract import AbstractTree, abstractmethod
class AbstractBinaryTree(AbstractTree):
    """
    AbstractBinaryTree is an abstract base class that extends AbstractTree and defines the interface for a binary tree.
    Subclasses must override the abstract methods to provide specific implementations.
    """
    @abstractmethod
    def left(self, pos):
        """
        Returns the position of the left child node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the left child node.
        """
        pass

    @abstractmethod
    def right(self, pos):
        """
        Returns the position of the right child node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the right child node.
        """
        pass

    def childern(self, pos):
        """
        Returns a list of positions of the children nodes of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            A list of positions of the children nodes.
        """

        if pos is None:
            return None
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)
            
    def sibling(self, pos):
        """
        Returns the position of the sibling node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the sibling node.
        """
        parent = self.parent(pos)
        if parent is None:
            return None
        if pos == self.left(parent):
            return self.right(parent)
        if pos == self.right(parent):
            return self.left(parent)