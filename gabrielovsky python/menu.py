elec=int(input("¿Que de desea hacer?\n0: Comparacion de numeros\n1: Suma\n2: Resta\n3: Divicion\n4: Multiplicacion\n5: Datos\n6: Multiplicacion de clase\n7: Salir \n"))
if elec==0:
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
elif elec==1:
    print("Suma de dos numeros")
    num1=int(input("Dame un numero "))
    num2=int(input("Dame otro numero "))
    suma=num1+num2
    print("El resultado de la suma es: ", suma)
    input()
elif elec==2:
    print("Resta de dos numeros")
    num1=int(input("Dame un numero "))
    num2=int(input("Dame otro numero "))
    suma=num1-num2
    print("El resultado de la suma es: ", suma)
    input()
elif elec==3:
    print("Division de dos numeros")
    num1=int(input("Dame el dividendo"))
    num2=int(input("Dame el divisor "))
    float(suma=num1/num2)
    print("El resultado de la division es: ", suma)
    input()
elif elec==4:
    print("Datos personales")
    nom=str(input("Ingrese su nombre: "))
    ed=int(input("Ingrese su edad: "))
    pes=float(input("Ingrese su peso: "))
    print("Nombre: ",nom,"\n", "Edad: ",ed, "\n", "Peso: ",pes, "\n")
    input()
elif elec==5:
    print("Multiplicacion de dos digitos ")
    num1=int(input("Dame el primer numero: "))
    num2=int(input("Dame el segundo numero: "))
    float(suma=num1*num2)
    print("El resultado de la division es: ", suma)
    input()
elif elec==6:
    n=int(input("Inserte hasta que numero se quiere multiplicar: "))
    tab=int(input("Inserta el numero del que quieres la tabla de multiplicar: "))
    for var in range (1,n+1):
        print(var, " x ",tab, " = ",var*tab)
    input()
elif elec==7:
    print("Adios :)")
