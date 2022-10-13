### 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

N = float(input('Input a number: '))
list = [int(ele) for ele in str(N) if ele.isdigit()]

print(list)

res = 0
for i in range(len(list)):
    res = res + list[i]
print(res)
