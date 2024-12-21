# Binary Tree Node Class

class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None
    
# Pre order traversal    
 def preorder(root):
   if root == None:
     return
   print(root.elem, end = ' ')
   preorder(root.left)
   preorder(root.right)
  
#  In order traversal  
 def inorder(root):
   if root == None:
     return

   inorder(root.left)
   print(root.elem, end = ' ')
   inorder(root.right)

#  Post order traversal 
 def postorder(root):
   if root == None:
     return

   postorder(root.left)
   postorder(root.right)
   print(root.elem, end = ' ')

