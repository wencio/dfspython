class Node:
 def __init__(self,data):
     self.data = data
     self.right = None
     self.left = None
     
def inorderTraversal(node):
     if node is not None:
         postorderTraversal(node.left)
         print(node.data)
         postorderTraversal(node.right)
         
         
 
# Ejemplo de arbol binario
 
root = Node(1)  
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

# Recorrido inorder,  primero se visitan todos los nodos del subárbol izquierdo en orden, luego se visita el nodo raíz y finalmente se visitan todos los nodos del subárbol derecho en orden. Este recorrido se utiliza comúnmente para obtener una lista
# ordenada de los nodos de un árbol binario de búsqueda.
print( "Recorrido inorder del arbol:")   
inorderTraversal(root)
