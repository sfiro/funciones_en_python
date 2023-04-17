#1- definición de la función normal
def increment(x):
  return x+10
#2- definición de la misma función ejecutada con lambda 
increment_v2 = lambda x:x+10

print("resultado de función normalmente definida")
print(increment(10))
print("resultado de función lambda")
print(increment_v2(10))

#3- high order function (usar una funcion desde una función)
def hof(x,func):
  return x+func(x)

hof_v2 = lambda x,func: x+func(x)

print("resultado de HOF")
print(hof(10,increment))

print("el resultado del HOF con lambda es:")
print(hof_v2(10,increment))