#break and continue, функции объявление и передача параметров, по значению

# Выход из цикла (break и continue)
for r in range(6):
    if r == 2 :
        continue
    if r == 4 :
        break
    print(f"Значение {r}")

#Синтаксис функции
# def имя_функции ([параметры]):
#     инструкции

#Вызов обязателен
#Вложенные функции : функция в функции

def say_hello():
    print("Hello")

say_hello()

def print_messages():
    #определение локальных функций(область видимости)
    def say_hello1(): print("Hello1")
    def say_hello2(): print("Hello2")
    say_hello1()
    say_hello2()

print_messages()

#Организация при помощи main()

def main():
    say_hello()
    print_messages()

def say_hello(name, age):
    print(f"Hello {name} {age}")
say_hello("Renata", 19)

#Параметры по умолчанию

def text(name ="Renata", age = 19):
    print(f"Hello {name} {age}")


def sum1(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum1(1, 2, 3, 4, 5)  # sum = 15
sum1(3, 4, 5, 6)  # sum = 18

