
# numero en un vector generado por un for 
number = []
for element in range(1,11):
    number.append(element)
print("valores con un ciclo normal")
print(number)

#numeros en un vector por list comprehension (facilidad de leer)

number_v2=[element*2 for element in range(1,11)]
print("valores del list comprehension")
print(number_v2)

# list comphension con condicional al final

number_v3 = [element for element in range(1,11) if element % 2 == 0 ]
print("se ejecuta el list comprehension con un conducional del módulo cero, devuelve solo numeros pares")
print(number_v3)