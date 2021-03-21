number = int(input("Введите целое положительное число: "))
bol_numb = 0
while number > 0:
    ostatok = number % 10
    if  ostatok > bol_numb:
        bol_numb = ostatok
    number //= 10
print(bol_numb)