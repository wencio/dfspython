class Node:
 def __init__(self,data):
     self.data = data
     self.right = None
     self.left = None
     
def postorderTraversal(node):
     if node is not None:
         print(node.data)
         postorderTraversal(node.left)
         postorderTraversal(node.right)
       
         
 
# Ejemplo de arbol binario
 
root = Node(1)  
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

# Recorrido preorder, recorre el arbol visitando primero el nodo raiz, 
# luego el subarbol izquierdo y finalmente el subarbol derecho
print( "Recorrido preorder del arbol:")   
postorderTraversal(root)