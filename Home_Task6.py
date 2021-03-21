#Шестое задание
a = float(input("Результат в первый день: "))
b = float(input("Нужный результат: "))
date = 1
while b >= a:
    a = a * 1.1
    date = date + 1
    print(f" {date}-й день: {round(a, 2)} км.")
print(f"Спортсмен достигент рехультата на {date}-й день")
