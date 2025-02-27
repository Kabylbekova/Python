# Модули и пакеты
# любой файл с разрешением .ру - модуль
# пакет - набор модулей (обязательно должен быть файл ____init___.py)


# Работа с файлами
# open - Функция которая открывает файл в определенном режиме 

# режимы
# r - read (только для чтения) 
# w - wriite (Только для записи каждый раз файл очищается)
# a - append (только для дозаписи добавляется в конец)
# x - создает файл но если он существует выйдет ошибка


# b - binary (в бинарном виде )-  >


"""read """


# file = open('text.txt', 'r')
# # print(dir(file))
# print(file.writable())
# print(file.readable())
# print(file.read())


def repeat_phrase_n_times(phrase, n):
    for i in range(n):
        print(phrase)
        
repeat_phrase_n_times