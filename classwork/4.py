
# Операции сравнения ==, !=, >=, >, <=, <
# Циклы while for

# while условное_выражение:
#    инструкции

s = 5
k = 7
if s == k:
    print(f"Правда")
else:
    print(f"Неправда")


number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Условие перестало быть истинным")
print("Работа программы завершена")

#for

# for переменная in набор_значений:
#     инструкции

message = "Hello"

for c in message:
    print(c)

#range()
# генерирует числовую последовательность

range(10)

for a in range(6, 10, 2):
    print(a)
else:
    print(f"Работа цикла завершена, последнее значение {a}")

# Вложенные циклы
#6 8

i = 1
j = 1

while i <  10:
    while j < 10:
        print(i*j, end = "\t")
        j += 1
    print("\n")
    j = 1
    i+=1
else:
    print(f"Таблица умножения выведена")

# Выход из цикла (break и continue)
for r in range(6):
    if r == 2 :
        continue
    if r == 4 :
        break
    print(f"Значение {r}")









