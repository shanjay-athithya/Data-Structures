from abc import ABC, abstractmethod
class AbstractTree:
    """
        Returns the height of the tree or the height of a subtree rooted at the specified position.

        Args:
            pos (optional): The position of the root of the subtree. If not specified, returns the height of the entire tree.

        Returns:
            The height of the tree or subtree.
        """
    @abstractmethod
    def root(self):
        """
        Returns the position of the root node in the tree.

        Returns:
            The position of the root node.
        """
        pass
    @abstractmethod
    def parent(self, pos):
        """
        Returns the position of the parent node of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The position of the parent node.
        """
        pass
    @abstractmethod
    def chilren(self, pos):
        """
        Returns a list of positions of the children nodes of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            A list of positions of the children nodes.
        """
        pass
    @abstractmethod
    def numchildren(self, pos):
        """
        Returns the number of children nodes of the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The number of children nodes.
        """
        pass
    @abstractmethod
    def __len__(self):
        """
        Returns the total number of nodes in the tree.

        Returns:
            The number of nodes in the tree.
        """
        pass
    def isRoot(self, pos):
        """
        Checks if the specified position is the root node.

        Args:
            pos: The position of the node.

        Returns:
            True if the position is the root node, False otherwise.
        """
        return pos == self.root
    def isLeaf(self, pos):
        """
        Checks if the specified position is a leaf node.

        Args:
            pos: The position of the node.

        Returns:
            True if the position is a leaf node, False otherwise.
        """
        return self.numchildren(pos) == 0
    def isEmpty(self):
        """
        Checks if the tree is empty.

        Returns:
            True if the tree is empty, False otherwise.
        """
        return len(self) == 0
    def Ndept(self, pos):
        """
        Returns the depth of the node at the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The depth of the node.
        """
        if self.isRoot(pos):
            return 0
        return 1 + (self.Ndept(self.parent(pos)))
    def Nheight(self, pos):
        """
        Returns the height of the node at the specified position.

        Args:
            pos: The position of the node.

        Returns:
            The height of the node.
        """
        if self.isLeaf(pos):
            return 0
        return 1 + max([self.Nheight(child) for child in self.children(pos)])
    def height(self, pos):
        """
        Returns the height of the tree or the height of a subtree rooted at the specified position.

        Args:
            pos (optional): The position of the root of the subtree. If not specified, returns the height of the entire tree.

        Returns:
            The height of the tree or subtree.
        """
        if pos is None:
            if self.isEmpty():
                return -1
            pos = self.root()
            return self.Nheight(pos)
        return self.Nheight(self.root())
