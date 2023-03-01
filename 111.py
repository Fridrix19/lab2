# 1 задание
password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")

if password == confirm_password:
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password):
        print("Пароль принят")
    else:
        print("Пароль должен содержать не менее 8 символов, как минимум одну заглавную и одну строчную букву")
else:
    print("Пароль не принят")


# 2 задание
seat_number = int(input("Введите номер места: "))

if seat_number % 2 == 0:
    print("Это верхнее место", end="")
else:
    print("Это нижнее место", end="")

if seat_number < 37:
    print(" в купе")
else:
    print(" в боковом отсеке")
# 3 задание
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Год {year} - високосный")
else:
    print("Это год не високосный")
#4 задание
color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("Фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color1 == "желтый" and color2 == "красный":
    print("Оранжевый")
elif color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий":
    print("Зеленый")
elif color1 == "синий" and color2 == "синий" or color1 == "синий" and color2 == "синий":
    print("синий")
elif color1 == "желтый" and color2 == "желтый" or color1 == "желтый" and color2 == "желтый":
    print("желтый")
elif color1 == "красный" and color2 == "красный" or color1 == "красный" and color2 == "красный":
    print("красный")
else:
    print("Ошибка: введите только 'красный', 'синий' или 'желтый'")

#5 задание
n = int(input("Сколько слов вы хотите ввести? "))
words = []

for i in range(n):
    word = input(f"Введите слово {i+1}: ")
    words.append(word)

result = " ".join(words)
print(result)
