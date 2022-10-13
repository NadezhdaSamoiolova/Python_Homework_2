##### 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  *Пример:*
#   - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Input N: "))
n = 1
res_list = []
for i in range(1, N + 1):
    n *= i 
    res_list.append(int(n))
print(f"Set of product of numbers from 1 to {N}:", res_list)