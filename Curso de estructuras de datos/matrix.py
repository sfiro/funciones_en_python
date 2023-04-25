from grid import Grid
from array import Array
import random

class Matrix3d():
    """ Esta función genera un array 3D, los parametros, filas, columnas y matrices y por último los valores
    get_heig  funcion para obtener las filas
    get_width funcion para obtener las columnas
    get_depth funcion para obtener las matrices 
    __str__ imprime las matrices con sus valores
    __random__ define numeros aleatorios en las matrices """
    def __init__(self,rows,columns,matrix,fill_value = None):
        self.data = Grid(rows,columns)
        for row in range(rows):
            for column in range(columns):
                self.data[row][column]= Array(matrix,fill_value)
    
    def get_heig(self):
        return self.data.get_height()
    
    def get_width(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __str__(self):
        result = ""
        for row in range(self.get_heig()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][column][depth]) + " "
                result += "\n"
            result += "\n"
            result += "\n"
        return str(result)
    
    def __random__(self):
        result = ""
        for row in range(self.get_heig()):
            for column in range(self.get_width()):
                for depth in range(self.get_depth()):
                    self.data[row][column][depth] = random.randint(1,100)
    



if __name__ == "__main__":
    #matrix = Grid(3,4)
    #print(matrix.__str__()) 
    m3 = Matrix3d(3,3,3)
    print(m3.get_heig())
    print(m3.get_width())
    print(m3.get_depth())
    m3.__random__()
    print(m3.__str__())