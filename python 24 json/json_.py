# '''### Тема: JSON в Python — зачем нужен и как работает

# ---

# ### 1. Что такое JSON?

# JSON (JavaScript Object Notation) — это формат обмена данными, который используется для представления структурированной информации.
#  JSON был создан на основе синтаксиса JavaScript, но сейчас является независимым от языка стандартом.  

# Он обладает следующими преимуществами:  
# - Простота: JSON легко читается как человеком, так и машиной.  
# - Компактность: структура данных минимальна, без лишних символов.  
# - Универсальность: JSON поддерживается большинством языков программирования (Python, Java, C++, и т.д.).  
# - Использование в веб-разработке: часто используется для обмена данными между сервером и клиентом (например, API).'''





# '''### 2. Зачем нужен JSON в Python?

# JSON необходим в Python для решения следующих задач:

# 1. Хранение данных:  
#    JSON используется для хранения конфигурационных файлов, настроек приложений и других данных, которые легко сериализовать и десериализовать.

# 2. Передача данных:  
#    При взаимодействии с веб-серверами или внешними API, данные передаются в формате JSON.

# 3. Конвертация данных:  
#    JSON позволяет преобразовывать сложные структуры Python (например, словари и списки) в текстовый формат и обратно.

# ---

# ### 3. JSON и Python: Основные возможности

# В Python для работы с JSON используется встроенный модуль *json. Он предоставляет функции для:Сериализацииии*
#  (преобразование Python объектов в JSON) Десериализацииии** (обратное преобразование из JSON в Python объекты)

# #Основные функции модуля jsonon*Функцияия*              Описаниеие**                                                    |
# |----------------------------|----------------------------------------------------------------|
# | json.dumps()             | Преобразует Python объект в строку JSON                        |
# | json.loads()             | Преобразует JSON строку в Python объект                       |
# | json.dump()              | Записывает JSON в файл                                         |
# | json.load()              | Читает JSON из файла и преобразует его в Python объект        |'''



# import json

# # Словарь Python
# data = {
#     "name": "Иван",
#     "age": 25,
#     "city": "Москва"
# }

# # Сериализация: из Python объекта в JSON строку
# json_string = json.dumps(data, ensure_ascii=False)
# print(type(json_string))
# print("JSON строка:", json_string)

# # Десериализация: из JSON строки в Python объект
# parsed_data = json.loads(json_string)
# print("Python объект:", parsed_data)
# print(type(parsed_data))



# #### *1. json.dumps() — Преобразует Python объект в строку JSON*

# import json

# # Python объект
# data = {"name": "Алексей", "age": 30, "city": "Санкт-Петербург"}

# # Преобразование в строку JSON
# json_string = json.dumps(data, ensure_ascii=False)


# #### *2. json.loads() — Преобразует JSON строку в Python объект*

# import json

# # JSON строка
# json_string = '{"name": "Мария", "age": 25, "city": "Москва"}'

# # Преобразование в Python объект
# data = json.loads(json_string)
# print("Python объект:", data)
# # *Вывод:*
# # Python объект: {'name': 'Мария', 'age': 25, 'city': 'Москва'}




# import json

# # Python объект
# data = {"name": "Иван", "age": 35, "city": "Москва"}

# # Преобразование в строку JSON
# json_string = json.dumps(data, ensure_ascii=False)
# print("JSON строка:", json_string)





# import json

# user = {
#    'user' : 'Aisha',
#    'age' : 12,
#    'city' : 'Talas'

# }
# underdums = json.dumps(user)
# print(underdums)
# print(type(underdums))

# userloads = json.loads(underdums)
# print(userloads)
# print(type(userloads))





strings = 'hello world'
integer = 1523
settype = {True, False, 'hello'}
dicttype = {'user': 'Aigul'}
listtype = [123, 'alina']
tupletype = ('burul', 1523)

print(type(strings))
print(type(integer))
print(type(settype))
print(type(dicttype))
print(type(listtype))
print(type(tupletype))




