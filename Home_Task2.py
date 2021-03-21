#Второе задание
seconds = int(input("Введите время в секундах: "))
minute = seconds // 60
hours = minute // 60
print(f"Время: {hours:02d}:{minute:02d}:{seconds % 60:02d}")
