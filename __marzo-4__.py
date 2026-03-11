


while True: 
    try:
        num =int(input("Dame el número: "))
        inverso = 1/num
        break 
    except ValueError:
        print("Pon bien el número wey")
    except ZeroDivisionError:
        print("Con el cero no se divide puto")    


print(f"El inverso de {num} es {inverso}")


# while True:
#     try:
#         num = int(input("Dame el número we: "))
#         break
#     except ValueError:
#         print(f"Porfa pon un número bien, pendejo")
# iter = 0
# while iter < 11:
#     print(f"{num} * {iter}= {num*iter}")
#     iter = iter + 1




