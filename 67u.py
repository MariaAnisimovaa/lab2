c1=input("Ввведите первый цвет")
c2=input("Введите второй цвет")

if (c1 != "Красный" or "Синий" or "Желтый") and (c2 != "Красный" or "Синий" or "Желтый"):
    print("Ошибка, введите основные цвета")
if (c1 == "Красный" or "Синий" or "Желтый") and (c2 == "Красный" or "Синий" or"Желтый"):
    if (c1 == "Красный" and c2 == "Синий") or (c1 == "Синий" and c2 == "Красный"):
            print("Вторичный цвет: Фиолетовый")
    if (c1 == "Красный" and c2 == "Желтый") or (c1 == "Желтый" and c2 == "Красный"):
            print("Вторичный цвет: Оранжевый")
    if (c1 == "Желтый" and c2 == "Синий") or (c1 == "Синий" and c2 == "Желтый"):
            print("Вторичный цвет: Зеленый")

