



"=============================Декораторы============================="
# функция высшего порядка - функция, которая принимает в аргументы функцию, 
# создает внутри себя функцию,
#  вызывает функцию и возвращает функцию
# декоратор - функция высшего порядка, которая нужна чтобы 
# расширять функционал функции не изменяя ее (функция обертка)

def decorator(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print('start:', datetime.now())
        func(*args, **kwargs)
        print('finish:', datetime.now())
    return wrapper

def hello():
    print('Hello world')

decorator(hello) ()
# decorator(hello) -> wrapper
# wrapper ()

wrapper = decorator(hello)
wrapper()



def funkiy():
    from datetime import datetime
    funk = print('start:', datetime.now())
    if funk:
        pass
    return funk

fun = funkiy()
print(fun)


    

"------------------------Синтаксический сахар------------------------"
# @

@decorator
def hello():
    print('Hello world')

hello()
# @decorator -> hello = decorator(hello)


@decorator
def my_sqrt(x):
    print(x**0.5)

my_sqrt(25)




def func_start_time(func):
    def wrapper(*a, **k):
        from datetime import datetime
        now = datetime.now()
        correct_format = now.strftime('%d.%m.%Y %H:%M')
        print('Функция запущена', correct_format)
        func(*a, **k)
    return wrapper

@func_start_time
def func():
    print('Hello world')
func()


def decorator(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator(5)
def hello():
    print('hello world!!!')

hello()



def simple_decor(func):
    def wrapper(*a, **k):
        print('Выполняется запрос...')
        result = func(*a, **k)
        print('Функция выполнена!')
        return result
    return wrapper 

@simple_decor
def say_hello():
    print('Привет мир!')
    
    
@simple_decor
def add_numbers(a, b):
    return a+b

say_hello()
print("Сумма: ", add_numbers(3, 5))

