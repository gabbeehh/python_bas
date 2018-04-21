"""
for i in range (50,89):
    print("Valor de i= ", i)
print("final")
input()
"""

n=int(input("Inserte hasta que numero se quiere multiplicar: "))
tab=int(input("Inserta el numero del que quieres la tabla de multiplicar: "))
for var in range (1,n+1):
    print(var, " x ",tab, " = ",var*tab)
input()
