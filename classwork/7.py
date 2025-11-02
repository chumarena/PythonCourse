#фунция - именованный блок кода, передача параметров

#* - символ, после которого передача параметров идет только по имени

def job(name = "Renata", age = 19, *, place = "Polytech"):
    print(f"name = {name}, age = {age}, place = {place}")

job(place = "Prorazvitie")
job("Renata", 18)
#job("Renata", 20, "Mistake")

print("\n")



#/ - определение параметров по позиции(параметрам до символа можно передать значение только по позиции)

def university(country = "", /, city = "Minsk", name = ""):
    print(f"country = {country}, city = {city}, name = {name}")

university("Russia", name  = "Polytech", city = "SPB")
university("Russia","SPB", "Polytech" )
#university(country = "Mistake")

print("\n")

#func(*параметр) - через параметр передаем неопределенное количество значений

def sum1(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum1(1, 2, 3, 4, 5)  # sum = 15
sum1(3, 4, 5, 6)  # sum = 18

print("\n")
#Возвращение результата функции

#Синтаксис

#def имя_функции([параметры]):
#   инструкции
#   return возвращаемое_значение

def get_message():
    return "Hello World!"

message = get_message()
print(message, get_message())

print("\n")

def multiply(num1, num2):
    return num1 * num2

print(multiply(2, 3))

print("\n")

#return - не только возвращает значение, но и выходит из функции

def available_age(age):
    if age > 20 or age < 1:
        return
    else:
        print(f"age = {age}")

age = int(input("age1 = "))
available_age(age)
available_age(int(input("age2 = ")))

