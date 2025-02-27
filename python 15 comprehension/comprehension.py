
# генератор с помощью которого мы можем создавать последовательности используя цикл for  в одну строку
# Результат for элемент in последовательность 
# Результат for элемент in последовательность if фильтр 



# comprehension = [i for i in range(1, 6)]
# print(comprehension)


# numbers = range(1, 101)
# for number in numbers:
#     print(number)
    



# even = [x for x in range(1, 21 ) if x % 2 == 0]
# print(even)
    
    

# positive_negative = ['Positive' if x > 0 else 'Negative' for x in range(-5, 6)]
# print(positive_negative)




# divisibl = [x for x in range(1, 31) if x % 3 == 0 or x % 5 == 0]
# print(divisibl)





# res1 = range(100)
# res2 = range(2, 11)
# res3 = range(2, 11, 2)

# print(list(res1))  # Печатает все числа от 0 до 99
# print(list(res2))  # Печатает [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(res3))  # Печатает [1, 3, 5, 7, 9]





# res1 = range(100)
# res2 = range(2, 11)
# res3 = range(2, 11, 2)

# for i2 in res2:
#     print(i2)
    
# for i1 in res1:
#     print(i1)
    
# for i3 in res3:
#     print(i3)
 
 
 
 
 
 
# list = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list.append(i)
#         print(list)


# lst = [("четное" if x % 2 == 0 else "нечетное") for x in range(1, 11)]
# print(lst)



# even = [x ** 2 for x in range(1, 6)]
# print(even)



dict1 = dict((i, i ** 2) for i in range(10))
dict2 = {i : i**2 for i in range(10)}
# print(dict2)
# print(dict1)


dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {value:key for key, value in dict1.items()}
# print(dict2)



user2 = {'user': {'Alina' : 12, 'Alisa': 32, 'Aibek':13}, 
         'car':{'BMW': 2024,'mersedes': 2022 }}  







