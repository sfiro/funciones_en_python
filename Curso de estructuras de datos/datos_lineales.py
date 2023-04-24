"funcion recursiva donde se crea una piramide impresa en la terminal"
def pyramid(lower,upper,margin=0):
    blanks = " " * margin
    print(blanks,lower,upper)
    if lower > upper:
        print(blanks,0)
        print("hola")
        return 0
    else:
        result = lower + pyramid(lower+1,upper,margin+4)
        print(blanks,result)
        return result

if __name__ == "__main__":
    pyramid(1,10)
