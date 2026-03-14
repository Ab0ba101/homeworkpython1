import random
name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(f"Hello {name}, you are {age}!")

age = int(input("Введіть ваш вік: "))
if age > 18:
    print("Login allowed!")
else:
    print("Login prohibited!")


number_to_guess = random.randint(1, 10)
attempts = 3

while attempts > 0:
    user_guess = int(input("Вгадайте число від 1 до 10: "))
    if user_guess > number_to_guess:
        print("Менше")
    elif user_guess < number_to_guess:
        print("Більше")
    else:
        print("Вітаємо! Ви вгадали число.")
        break
    attempts -= 1

if attempts == 0:
    print(f"На жаль, ви програли. Загадане число було {number_to_guess}.")

from_num = int(input("Введіть число 'від': "))
to_num = int(input("Введіть число 'до': "))
for i in range(from_num, to_num + 1):
    print(i, end=' ')

n = int(input("Введіть число n: "))
for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=' ')

n = int(input("Введіть число для обчислення факторіалу: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал {n} = {factorial}")
а
points = int(input("Введіть кількість балів: "))
if 0 <= points < 50:
    print("Незадовільно")
elif 50 <= points < 70:
    print("Задовільно")
elif 70 <= points < 90:
    print("Добре")
elif 90 <= points <= 100:
    print("Відмінно")
else:
    print("Неправильна кількість балів")

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть операцію (+, -, *, /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        print("Ділення на нуль.")
    else:
        result = a / b
else:
    print("Неправильна операція.")

if operation in ['+', '-', '*', '/'] and not (operation == '/' and b == 0):
    print(f"Результат: {result}")
