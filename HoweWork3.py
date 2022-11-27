#Задача 3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random
def secondlist(firstlist):
    list = firstlist[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [1,2,3,4,5]
shufflelist = secondlist(list)
print("Первичный список: ")
print(list)
print("Перемешанный список: ")
print(shufflelist)