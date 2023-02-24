
class Node:
 def __init__(self,data):
     self.data = data
     self.right = None
     self.left = None
     
def postorderTraversal(node):
     if node is not None:
         postorderTraversal(node.left)
         postorderTraversal(node.right)
         print(node.data)
         
 
# Ejemplo de arbol binario
 
root = Node(1)  
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

# Recorrido postorden, primero los hijos izquierdos, luego los hijos derechos y finalmente el nodo raíz. Esto significa que se visitan todos 
# los nodos descendientes de un nodo antes de visitar el propio nodo.
print( "Recorrido postorden del arbol:")   
postorderTraversal(root)