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
