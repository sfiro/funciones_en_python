import random
from functools import reduce

class Array:
    """clase para crear array con las funciones encapsuladas 
    __len__ verifica el tamaño 
    __str__ retorna el array en versión str
    __iter__ retorna el iterador del array
    __getitem__ retorna el elemento indicando su indice 
    __setitem__ reemplaza el item en la posicion definica con el indice 
    __random__ genera elementos aleatorios enteros dentro del array
    __suma__ suma todos los elementos internos del array  """

    def __init__(self,capacity,fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
        
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self,index):
        return self.items[index]
    
    def __setitem__(self,index,new_item):
        self.items[index] = new_item
    
    def __random__(self):
        #for i in range(len(self.items)):
        #    self.__setitem__(i , random.randint(1,10))
        [self.__setitem__(i,random.randint(1,100)) for i in range(len((self.items)))]
        return self.items
    
    def __suma__(self):
        suma = 0
        #for i in range(len(self.items)):
        #    suma = suma + self.__getitem__(i)

        suma=reduce(lambda retorno,valor:retorno+valor,self.items)    
        return suma
        
        
if __name__ == "__main__":
    menu = Array(5)
    menu.__random__()
    print(menu.__str__())
    print(menu.__suma__())
    

    