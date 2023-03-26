print('hellow!')

def hello(a):
    print(a)

hello('Hi!')

# Вывести на экран сумму четных чисел от 1 до 100 включительно, используя функцию range()
sum = 0
for i in range(1,101):
    if i%2 == 0:
        sum += i
print(sum)