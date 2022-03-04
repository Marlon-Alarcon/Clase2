from api.library import *

def main():
    salario_min = 1000000
    sub_alim = 120000
    sub_transp = 80000
    bono = 50000
    nombre = input("digte el nombre ==>  ")
    salario = int (input("Digite el salario ==>  "))
    diastrabajados = int (input("Digite los dias trabajadas ==>  "))
    sueldoPagar = calcularsueldo(salario,diastrabajados)

    if salario < (salario_min * 2):
        sueldoPagar = sueldoPagar + sub_alim + sub_transp
    
    else: 
        sueldoPagar = sueldoPagar + bono

    print (f"Mi nombre es: {nombre} y mi sueldo a pagar es {sueldoPagar:.0f}")


if __name__ == "__main__":
    main()