# uso de dictionary comprehension

import random
countries = ['col','mex','bol','pe']
population ={}

for country in countries:
  population[country]= random.randint(1,100)

print("imprime el diccionario con los elementos aleatorios")
print(population)


populationV2 = {country:random.randint(1,100) for country in countries}
print("uso de dictionary comprehension")
print(populationV2)


# organizar dato en list comprehension

names = ['nico','zule','santi']
ages = [12,56,98]

datos = {names[i]:ages[i] for i in range(len(names)) }
print("datos organizados en dictionary comprehension")
print(datos)

# metodo para unir dos elementos en lista de tuplas
print(list(zip(names,ages)))  
datos ={name:age for (name,age) in zip(names,ages)}
print("datos definidos con ZIP")
print(datos)


# utilizar condicionales en dictionary comprehension
populationV1 = {country:random.randint(1,101) for country in countries}
print("valores de llave ")
print(populationV1)

result = {country:population for (country,population) in populationV1.items() if population>50}
print("valores mayores a 50")
print(result)

text = 'hola, soy debbie'
unique = {c:c.upper() for c in text if c in 'aeiou'}
print("llave valor dentro del texto")
print(unique)