profit = float(input("Укажите значение выручки: "))
cost = float(input("Укажите издержки фирмы: "))
if profit > cost:
    difference = profit - cost
    print(f"Компания имеет прибыль: {difference}")
    profitab = difference / profit
    print(f"Рентабельность составила: {profitab}")
    pers = int(input("Введите количество персонал: "))
    profitab_pers = profitab/pers
    print("Выручка на одного сотрудника: ", round(profitab_pers, 2))
elif profit == cost:
    print(f"Компания покрывает свои расходы полностю, без прибыли")
else:
    print(f"Компания имеет убыток: {profit - cost}")

