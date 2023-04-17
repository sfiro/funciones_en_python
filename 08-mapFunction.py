# la función map itera sobre todos los elementos y los transforma segun la función definida

number = [1,2,3,4]

number2 = list(map(lambda x:x*2,number))
print("la salida de la función map es:")
print(number2)

#la función map puede iterar sobre varias listas

numeros1 = [10,20,30,40]

numeros2 = [100,200,300]

salida = list(map(lambda x,y: x+y,numeros1,numeros2))

print("la salida de la función map sobre dos vectores es:")
print(salida)


#extraer datos de una lista de diccionarios
items = [
  { 'producto' : 'pantalon',
    'precio' : 100     },
  { 'producto' : 'camisa',
    'precio' : 200     },
  { 'producto' : 'gafas',
    'precio' : 300     }
]

valores = list(map(lambda valor:valor['precio'],items))
print("extrae los valores definidos en en listas de estructuras")
print(valores)

#agregar valores en una lista de disccionarios

def agregar(dicc):
  nuevo_dicc = dicc.copy()   # <<< ----- Es necesario para no transformar el listado original 
  nuevo_dicc['impuesto'] = nuevo_dicc['precio']*0.19
  return nuevo_dicc

dicc2 =list(map(agregar,items))
print("agregar los elementos dentro de la lista")
print(dicc2)

print(items)