# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {'col', 'mex', 'bol'}
print (set_countries)

# si yo pongo algo repetido, él me lo quita al imprimir
set_countries2 = {'col', 'mex', 'bol', 'col'}
print (set_countries2) # {'col', 'mex', 'bol'}

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, 'hola', False, 12.12}
print(set_types) # {False, 1, 12.12, 'hola'}

# la podemos crear a partir de un string
set_from_string = set('hoola')
print (set_from_string) # {'a', 'l', 'o', 'h'}

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)
print (set_numbers) # {1, 2, 3, 4}
# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)


###----------------Modificación de conjuntos ------------------

# evaluar el tamaño del conjunto
size = len(set_countries)
print(size)

# evaluar si un elemento se encuentra dentro de un conjunto
print('col' in set_countries)

# agregar un elemento al conjunto
set_countries.add("pe")
print("adiciona el dato 'pe' al conjunto ")
print(set_countries)
set_countries.add("bol")
print("adiciona el dato 'bol' al conjunto ")
print(set_countries)

#update
set_countries.update({'ar','ecua','pe'})
print("agrega un conjunto de datos a un conjunto previo ")
print(set_countries)

#remover
set_countries.remove('col')
print("elimina el elemento 'col' si no existe marca error ")
print(set_countries)

#remover sin error de falta de elemento
set_countries.discard('arg')
print("elimina el elemento 'arg' si no existe no marca error ")
print(set_countries)

#eliminar todos los elementos 
set_countries.clear()
print("elimina todos los elementos del conjunto")
print(set_countries)


## ------------- operaciones con conjuntos -------------------


set_a = {'col','mex','bol'}
print("conjunto A:")
print(set_a)
set_b = {'pe','bol'}
print("conjunto B:")
print(set_b)

# union de los conjuntos

set_c = set_a.union(set_b)
print("union de conjuntos A y B")
print(set_c)
print(set_a | set_b)

# interseccion

set_c = set_a.intersection(set_b)
print("intersección de conjuntos A y B")
print(set_c)
print(set_a & set_b)

#diferencia entre conjuntos

set_c = set_a.difference(set_b)
print("diferencia entre conjuntos A y B")
print(set_c)
print(set_a-set_b)

#diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print("la diferencia simetrica entre los conjuntos A y B (tomar los conjuntos y eliminar la interseccion")
print(set_c)
print(set_a ^ set_b)