num=int(input("Dame un numero: "))
num2=int(input("Dame un numero: "))
if num == num2:
    print("El numero ",num, " es igual al numero ", num2)
else:
    if num<num2 and num !=num2:
        print(num2, "es mayor que ", num, " y diferentes uno de otro")
    else:
        if num>num2 and num !=num2:
            print(num, "es mayor que ", num2, " y diferentes uno de otro")

input()
