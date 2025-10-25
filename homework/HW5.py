a = input("Введите число: ")
sum_digits = 0

for i in a:
    sum_digits += int(i)

if sum_digits % 3 == 0:
    print(f"Да")
else:
    print(f"Нет")
