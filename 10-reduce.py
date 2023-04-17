#función reduce siempre lleva la lista a un unico elemento y siempre va a tener el contador y el item, el contador es el resultado del Return 
import functools

numbers = [1,2,3,4]

result = functools.reduce(lambda contador,item:contador+item, numbers)
print("el resultado de la función lambda con reduce es:")
print(result)

def accum(contador,item):
    print("contador -->",contador)
    print("item -->",item)
    return contador + item
result = functools.reduce(accum, numbers)
