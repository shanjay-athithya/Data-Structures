from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def getroot(self):
        pass

    @abstractmethod
    def parent(self, pos):
        pass

    @abstractmethod
    def children(self, pos):
        pass

    def isroot(self, pos):
        return pos == self.root

    def isleaf(self, pos):
        return self.numchildren == 0

    def Ndepth(self, pos):
        if self.isroot(pos):
            return 0
        return 1 + self.Ndepth(self.parent(pos))

    def Nheight(self, pos):
        if self.isleaf(pos):
            return 0
        return 1 + max([self.Nheight(child) for child in self.children(pos)])


class Abstracttree(Abstract):
    @abstractmethod
    def left(self, pos):
        pass

    @abstractmethod
    def right(self, pos):
        pass

    def children(self, pos):
        if pos is not None:
            if self.left(pos) is not None:
                yield self.left(pos)
            if self.right(pos) is not None:
                yield self.right(pos)

    def sibling(self, pos):
        parent = self.parent(pos)
        if pos == self.left(parent):
            return self.right(parent)
        if pos == self.right(parent):
            return self.left(parent)


class Binarytree(Abstracttree):
    class Btnode:
        __slots__ = ['item', 'left', 'right', 'parent']

        def __init__(self, item, left=None, right=None, parent=None):
            self.item = item
            self.left = left
            self.right = right
            self.parent = parent

        def setitem(self, item):
            self.item = item

        def getiten(self):
            return self.item

    def __init__(self, item, Tleft=None, Tright=None, parent=None):
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
        if self.root is None:
            self.root = self.Btnode(item)
            self.size = 1
            return self.root
        else:
            raise ValueError("already root")

    def parent(self, pos):
        return pos.parent

    def left(self, pos):
        return pos.left

    def right(self, pos):
        return pos.right

    def getroot(self):
        return self.root

    def getleft(self, pos):
        return self.left(pos)

    def getright(self, pos):
        return self.right(pos)

    def addleft(self, pos, item):
        if self.getleft(pos) is None:
            pos.left = self.Btnode(item, parent=pos)
            self.size += 1
        else:
            raise ValueError('already a left element exists')

    def addright(self, pos, item):
        if self.getright(pos) is None:
            pos.right = self.Btnode(item, parent=pos)
            self.size += 1
        else:
            raise ValueError('already a right element exists')

    def preorder(self, pos):
        """
        Performs a preorder traversal of the tree starting from the specified position.

        Args:
            pos: The position from which the traversal should start.
        """
        res = f"[{pos.item}"
        if pos.left is not None:
            res += self.preorder(pos.left)
        if pos.right is not None:
            res += self.preorder(pos.right)
        res += "]"
        return res


if __name__ == '__main__':
    tree = Binarytree(0)
    tree.addleft(tree.root, 10)
    tree.addright(tree.root, 20)
    tree.addleft(tree.root.left, 30)
    tree.addright(tree.root.left, 40)
    tree.addleft(tree.root.right, 50)
    print("The original tree:")
    print(tree.preorder(tree.getroot()))
