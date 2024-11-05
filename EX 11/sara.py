from binarytree import BinaryTree
class Binarysearchtree(BinaryTree):
    def __init__(self,item=None,t_left=None,t_right=None):
        super().__init__(item,t_left,t_right)
    
    def Construct(self,item,pos):
        if pos is None:
            self.addRoot(item)

        elif item < pos.item :
            if pos.left is  None :
                pos.left = self.addLeft(item,pos) 
            else:
                self.Construct(item,pos.left)
        
        elif item > pos.item:
            if pos.right is None:
                pos.right = self.addRight(item,pos)
            else:
                self.Construct(item,pos.right)
    
    def search(self,item,pos):
        if pos is None:
            return None
        if item < pos.item :
            return self.search(item,pos.left)
        if item > pos.item :
            return self.search(item,pos.right)
        if item ==pos.item :
            return pos
        
    def findmax(self,pos):
        if pos is None:
            return None
        if pos.right is not None:
            return self.findmax(pos.right)
        else:
            return pos.item
            

    def findmin(self,pos):
        if pos is None:
            return None
        if pos.left is not None:
            return self.findmin(pos.left)
        else:
            return pos
        
    def delete(self,item):
        pos =self.search(item,self.root)
        if pos is None:
            return None

        parent=pos.parent
        #no child
        if pos.left is None  and pos.right is None :

            if parent.left == pos :
                parent.left = None
                return
            elif parent.right ==pos :
                parent.right =None
                return 
        # 1 child
        elif pos.left is not None and pos.right is None :
            parent.left =pos.left
            pos.parent =pos.left =pos.right =None   

        elif pos.right is not None and pos.left is None :
            parent.right =pos.right
            pos.parent =pos.left =pos.right =None  

        else:
            inorder_successor=self.findmin(pos.right)
            pos.item=inorder_successor.item
            parent=inorder_successor.parent
            parent.right =None
            return 

            
           
            
            

            
        
        

b=Binarysearchtree(10)
b.Construct(5,b.root)
b.Construct(11,b.root)
b.Construct(15,b.root)
b.Construct(1,b.root)
b.Construct(6,b.root)


print(b)

print(b.search(5,b.root))

print("max ele=",b.findmax(b.root))
print("mim ele=",b.findmin(b.root))

print(b)
b.delete(10)
print(b)

