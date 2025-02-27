



# # 1-6
# a = int(input("Введите первое число:  "))
# b = int(input("Введите второе число:  "))
# s = input('Выберите -> +, -, *, **, /, // :  ')

# def calculator(a, b, s):
#     if s == '+':
#         resulat = a + b
#     elif s == '-':
#         resulat = a - b
#     elif s == '*':
#         resulat = a * b
#     elif s == '**':
#         resulat = a ** b
#     elif s == '/':
#         resulat = a / b
#     elif s == '//':
#         resulat = a // b
#     else:
#         print(f'Такого символа нет{s}')
#     return f'resulat numbers ->{resulat}'

# cal = calculator(a, b, s)
# # print(cal)





# # 7

# def is_even(num):
#     return num % 2 == 0

# num = int(input("Введите число: "))
# print(f"Число {num} является четным." if is_even(num) else f"Число {num} является нечетным.")




# 8

# def compare_numbers(a, b):
#     if a > b:
#         return f"Число {a} больше числа {b}."
#     elif a < b:
#         return f"Число {b} больше числа {a}."
#     else:
#         return "Оба числа равны."

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(compare_numbers(a, b))



# # 9
# def max_of_three(a, b, c):
#     return max(a, b, c)

# a, b, c = map(int, input("Введите три числа через пробел: ").split())
# print("Максимальное число:", max_of_three(a, b, c))


# # 10
# def min_of_three(a, b, c):
#     return min(a, b, c)

# a, b, c = map(int, input("Введите три числа через пробел: ").split())
# print("Минимальное число:", min_of_three(a, b, c))



# # 11
# def sum_to_n(N):
#     return sum(range(1, N + 1))

# N = int(input("Введите число N: "))
# print("Сумма от 1 до N:", sum_to_n(N))


# 12

# def product_to_n(N):
#     result = 1
#     for i in range(1, N + 1):
#         result *= i
#     return result

# N = int(input("Введите число N: "))
# print("Произведение от 1 до N:", product_to_n(N))



# # 13
# def fibonacci_sequence(N):
#     fib = [0, 1]
#     for i in range(2, N):
#         fib.append(fib[-1] + fib[-2])
#     return fib[:N]

# N = int(input("Введите количество чисел Фибоначчи: "))
# print("Первые числа Фибоначчи:", fibonacci_sequence(N))



# # 14
# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(abs(num)))

# num = int(input("Введите число: "))
# print("Сумма цифр:", sum_of_digits(num))



# 15

# def reverse_number(num):
#     return int(str(num)[::-1]) if num >= 0 else -int(str(abs(num))[::-1])

# num = int(input("Введите число: "))
# print("Число в обратном порядке:", reverse_number(num))




# # 16
# def count_digits(num):
#     return len(str(abs))

# num = int(input("Введите число:  "))
# print("Количество цифр:", count_digits(num))


# 17

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# num = int(input("Введите число: "))
# print("Число является простым:", is_prime(num))



# # 18

# def find_divisors(num):
#     return [i for i in range(1, num + 1) if num % i == 0]

# num = int(input("Введите число: "))
# print("Делители числа:", find_divisors(num))


# # 19
# def find_position_in_sequence(N):
#     sequence = list(range(1, 101))
#     try:
#         return sequence.index(N) + 1
#     except ValueError:
#         return "Число не входит в диапазон от 1 до 100."

# N = int(input("Введите число: "))
# print("Позиция числа в последовательности:", find_position_in_sequence(N))



# 20


# num = int(input("Enter a number: "))


# for digit in str(num):
#     digit = int(digit) 
#     if digit % 2 == 0:
#         print(f"{digit} -> четное число")
#     else:
#         print(f"{digit} -> нечетное число")



# 21

# def find_pairs_with_sum(N):
#     pairs = [(i, N - i) for i in range(N // 2 + 1)]
#     return pairs

# N = int(input("Введите целое число N: "))
# print(find_pairs_with_sum(N))


# # 22
# user = int(input('enter number:  '))
# N = 46
# if user == N:
#     print(f"True {'true'}")
# else:
#     print(f"False {'false'}")

# # 23

# def sort_numbers():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     numbers = [int(input(f"Число {i+1}: ")) for i in range(N)]
#     return sorted(numbers)

# print("Отсортированные числа:", sort_numbers())




# 24


# def sum_until_negativ():
#     numbers = []
#     while True:
#         num = int(input("Введите число: "))
#         if num < 0:
#             break
#         numbers.append(num)
#     return sum(numbers)

# print("Сумма чисел до первого отрицательного:", sum_until_negativ())


# # 25
# def count_positive_negative():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     positive = negative = 0
#     for i in range(N):
#         num = int(input(f"Число {i+1}: "))
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1
#     return positive, negative

# pos, neg = count_positive_negative()
# print(f"Положительных чисел: {pos}, Отрицательных чисел: {neg}")



# 26

# def remove_number():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     numbers = [int(input(f"Число {i+1}: ")) for i in range(N)]
#     to_remove = int(input("Введите число для удаления: "))
#     numbers = [num for num in numbers if num != to_remove]
#     return numbers

# print("Список после удаления:", remove_number())



# # 27
# def sum_of_elements():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     numbers = [int(input(f"Число {i+1}: ")) for i in range(N)]
#     return sum(numbers)

# print("Сумма всех чисел:", sum_of_elements())




# # 28
# def average():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     numbers = [int(input(f"Число {i+1}: ")) for i in range(N)]
#     return sum(numbers) / len(numbers)

# print("Среднее арифметическое:", average())



# # 29
# def separate_even_odd():
#     N = int(input("Сколько чисел вы хотите ввести? "))
#     numbers = [int(input(f"Число {i+1}: ")) for i in range(N)]
#     even = [num for num in numbers if num % 2 == 0]
#     odd = [num for num in numbers if num % 2 != 0]
#     return even, odd

# even, odd = separate_even_odd()
# print("Четные числа:", even)
# print("Нечетные числа:", odd)


# 30. Проверка на палиндром.

# while True:
#     def is_palindrome():
#         num = input("Введите целое число: ")
#         return num == num[::-1]

#     print("Число является палиндромом:", is_palindrome())

