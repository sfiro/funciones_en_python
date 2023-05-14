
class Node():
    """ Funcion para definir un nodo (estructura de datos) donde se reciben dos parametros, el valor y la referencia al siguiente nodo"""
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":

    "Creación de nodos interconectados"
    nodo1 = None
    nodo2 = Node("A",None)
    nodo3 = Node("B",nodo2)
    print('Valor del nodo 2 es: ' + nodo2.data)
    
    print('El valor al que apunta el nodo 2 es: ')
    print(nodo2.next)

    print('Valor del nodo 3 es: ' + nodo3.data)
    print('El valor al que apunta el nodo 3 es: ')
    print(nodo3.next.data)
    nodo1 = Node("C",nodo3)
    print(nodo1.data)
    print(nodo1.next.data)
   
    head=None
    for i in range(1,5):
        print(i)
        head = Node(i,head)
    
    while head != None:
        print(head.data)
        head = head.next
