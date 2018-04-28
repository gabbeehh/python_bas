def menu():
    elec=int(input("¿Que de desea hacer?\n1: Suma\n2: Resta\n3: Multiplicacion\n4: Divicion\n5: Comparacion de numeros\n6: I.V.A.\n7: Tabla de mutiplicar\n8: Salir \n"))
    return int(elec)
loop=1
elec=0
while loop==1:
    elec=menu()
    if elec==1:
        print("Suma de dos numeros")
        num1=int(input("Dame un numero: "))
        num2=int(input("Dame otro numero: "))
        suma=num1+num2
        print("El resultado de la suma es: ", suma)
        input()
    elif elec==2:
        print("Resta de dos numeros")
        num1=int(input("Dame un numero: "))
        num2=int(input("Dame otro numero: "))
        suma=num1-num2
        print("El resultado de la suma es: ", suma)
        input()
    elif elec==3:
        print("Multiplicacion de dos numeros")
        num1=int(input("Dame un numero: "))
        num2=int(input("Dame otro numero: "))
        mult=(num1*num2)
        print("El resultado es: ",mult)
    elif elec==4:
        print("Division de dos numeros")
        num1=int(input("Dame el dividendo: "))
        num2=int(input("Dame el divisor: "))
        div=num1/num2
        print("El resultado de la division es: ", div)
        input()
    elif elec==5:
        print("Comparacion de numeros")
        a=int(input("Dame un numero: "))
        b=int(input("Dame un numero: "))
        c=int(input("Dame un numero: "))
        if (a==b and b==c):
            print("Los tres numeros son iguales")
        elif(a==b and a!=c):
            print(a, " es diferente de ", c , " e igual a ", b)
        elif(b==c and b!=a):
            print(b, " es diferente de ", a , " e igual a ", c)
        elif(c==a and c!=b):
            print(c, " es diferente de ", b , " e igual a ", a)
        elif(a>b and a>c):
            print(a, "es el mayor de los numeros")
        elif(b>a and b>c):
            print(b, "es el mayor de los numeros")
        elif(c>a and c>b):
            print(c, " es el mayor de los numeros")
        input()
    elif elec==6:
        print("Calcular el I.V.A.")
        iva=float(input("Ingrese el porcentaje a calcular de I.V.A: "))
        cant=float(input("Ingrese la cantidad: "))
        #Calculando el iva
        total=float(cant*(iva*0.01))
        print("La el iva de ",cant, "es", total)
        input()
    elif elec==7:
        n=int(input("Inserte hasta que numero se quiere multiplicar: "))
        tab=int(input("Inserta el numero del que quieres la tabla de multiplicar: "))
        for var in range (1,n+1):
            print(var, " x ",tab, " = ",var*tab)
        input()
    elif elec==8:
        loop=0
