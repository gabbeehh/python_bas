var=",genero: hombre"
lista=["Fernando Gabriel Cruz Vazquez, ", 20, "años, numero de cuenta", 314114714, var]

nombre="Gabriel"
apellido="Vazquez"
estat=1.75
nCuenta=314114714
gen="Masculino"
lista2=[nombre, apellido, estat, nCuenta, gen]
tamanio=len(lista2)
tipo=type(lista2)
lista2.append("Hello") #añade un elemento a la lista
print(lista2, "\n", tamanio, "\n", tipo)
#print(lista2.index(estat)) #dice en que posicion esta lo que indicaste ej 0,1,2
#print(lista2.count(gen))

input()
