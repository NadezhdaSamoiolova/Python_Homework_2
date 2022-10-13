























# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # Пример:
# #

# n = int(input("Введите целое положительное число N: "))
# res_list = []
# sum1 = 0
# for i in range(1, n + 1):
#     res_list.append(round(((1 + 1/i) ** i), 2))
#     sum1 += round(((1 + 1/i) ** i), 2)
# print(f"Для N = {n} последовательность чисел: {res_list} \nСумма чисел последовательности равна {sum1}")


# # Реализуйте алгоритм перемешивания списка.
# import random 

# n = int(input("Введите количество элементов: "))
# input_list = [i for i in range(n)]
# result_list = input_list[:]
# for i in range(n):
#     index_random = random.randint(0, n - 1)
#     result_list[i], result_list[index_random] = result_list[index_random], result_list[i]
#     # temp = result_list[i]
#     # result_list[i] = result_list[index_random]
#     # result_list[index_random] = temp
# print("Исходный список",input_list)
# print("Перемешанный список",result_list)



# import random
# a = [1, 2, 3, 4, 10, 11, 23, 56]
# random.shuffle(a, random.random)
# print(a)


# # Реализуйте алгоритм перемешивания списка.
# import random 
# import copy

# # n = int(input("Введите количество элементов: "))
# # input_list = [i for i in range(n)]
# # result_list = copy.deepcopy(input_list)
# # #result_list = input_list[:]
# # random.shuffle(result_list)
# # # for i in range(n):
# # #     index_random = random.randint(0, n - 1)
# # #     result_list[i], result_list[index_random] = result_list[index_random], result_list[i]
# #     # temp = result_list[i]
# #     # result_list[i] = result_list[index_random]
# #     # result_list[index_random] = temp
# # print("Исходный список",input_list)
# # print("Перемешанный список",result_list)

# my_list = [[1, 2], [3, 4]] # вложенный список
# #my_list2 = my_list[:]
# my_list2 = copy.deepcopy(my_list)
# my_list[0].append(5)
# print(my_list2)


# positions = []
# with open('file.txt', 'r', encoding='utf-8') as f:
#     positions = f.read().split()
#     positions = [int(i) for i in positions]
# n = int(input('Введите целое число: '))
# s = []
# for i in range(-n, n + 1):
#     s.append(i)
# result = 1
# for i in range(len(positions)):
#     result *= s[positions[i] - 1]
# print(f'Исходный список: {s}.\nПозиции: {positions}.')
# print(result)

# #with open(r'С:\nfile.txt', 'r', encoding='utf-8') as f:
# #with open('С:\\nfile.txt', 'r', encoding='utf-8') as f:
# with open('С:/Program Files/nfile.txt', 'r', encoding='utf-8') as f: