



# try - анализ 
# except- исключение
# finally



# try:
#     print(x)
# except NameError:
#   print("Вы не определили переменную")


  # a = input('какой язык ')
# if a.lower() == 'python':
#     print('да')
# else:
#     print('нет')




# a = int(input("Сколько вам лет?"))
# if 7 <= a <12:
#   print("Вы получите бесплатный чай. ")
# elif 13 <= a < 18:
#   print('Вы получите бесплатную воду.')
# elif 18 <= a <= 65:
#   print("Вы получите бесплатный кофе.")


# name = 'Jone'
# age = 13
# name1 = 'Валодя'
# age1 = 24
# name2 = 'Максим'
# age2 = 65
# a = input('Напишите свое имя...')
# if a == name or a == age:
#   print('Вам отказано купить энергетики!')
# elif a == name1 or a == age1:
#   print('Удачной покупки!')
# elif a == name2 or a == age2:
#   print('Удачной покупки, напоминаем в таком возрасте много пить нельзя!')



# try:
#   a = int(input('Введите свой возраст: '))
  
#   if a < 18:
#     print('Извините, мы не можем вас принять на работу.')
#   elif 18 <= a < 36:
#     print("Вы приняты на работу.")
#   else:
#     print("Мы не берем на работу людей старше 36.")
  
# except ValueError:
#   print('Вы ввели текст, а не возраст!')
  
  

x = 0
while x == 0

  try:
    x = int(input("введите число: "))
    x += 5
    print(x)
  except ValueError:
    print('Введите число:  ')
    
    