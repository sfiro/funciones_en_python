from array import Array
import random

class Grid():
    """"array bidimensional con métodos internos parametros: filas, columnas y datos
    get_height devuelva el valor de la altura
    get_width  devuelve el valor del ancho de la matriz
    __getitem__ devuelve el item asociado a la fila (este es un array tambien)
    __str__ devuelve la representación del array en formato str
    --random__ llena el array con valores aleatorios enteros """
    def __init__(self,rows,columns,fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns,fill_value)
    
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self,index):
        return self.data[index]
    
    def __str__(self):
        result = "" 

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"
        
        return str(result)
    
    def __random__(self):
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(1,100)


if __name__ == '__main__':
    vector = Array(5,1)
    print(vector.__str__())
    matrix = Grid(5,5,8)
    matrix.__random__()
    print(matrix)