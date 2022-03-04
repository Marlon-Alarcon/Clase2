# Manejo de Listas

""" ****************************************
----------- Manejo de Listas ----------
**************************************** """

from re import I


def listas():
    lista1 = []
    lista2 = list()

    listaConElementos = [30, 2000000, "Ing Sistemas", "Marlon", "Estudiante", True, ["Magister", "Doctorado", "Especializacion", "Años de experiencia", 20]]

    # print(listaConElementos[1]) # un elemento

# Utilizando el ciclos

    # for i in range(6): #la cantidad de elementos de la lista
    #     print(listaConElementos[i])

    # for i in range(len(listaConElementos)): #Obtiene el tamaño del arreglo
    #     print(listaConElementos[i])
    
    # print("")
    # print("")
    # print("")
    # print("Mostrando Elementos con ciclo while")

    # j=0

    # while j < len(listaConElementos):
    #     print(listaConElementos[j]) #va j
    #     j = j + 1

    listaConElementos[1] = listaConElementos[1] + 200000 # aumentamos 200.000

    print(listaConElementos[6][3]) # que me muestre el ultimo elemento forma 1
    print(listaConElementos[-1][3]) #que me muestre el ultimo elemento
    print(listaConElementos[0:3]) # le defino rango - muestra la posicion de la 0 hasta la 3
#pares
    print(listaConElementos[1:6:2])

#Impares
    print(listaConElementos[0:6:2])

    # listaConElementos.append("Sede Riohacha") #agregar un elemento a lo ultimo de la lista
    # print(listaConElementos)

    # listaConElementos.append(["sede riohacha", "Miguel"]) #agregar un arreglo
    # print(listaConElementos)

    listaConElementos.insert(2, [ "Sede Riohacha", "Miguel"]) #agregar un elemento en la posicion que quiera
    print(listaConElementos)

    # del listaConElementos[2] #elimina elemento de la posicion x
    # print(listaConElementos)

    listaConElementos.remove("Estudiante")
    print(listaConElementos)

def main():
    listas()

if __name__ == "__main__":
    main()