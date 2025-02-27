


name = input('Enter name: ')
age = int(input('Enter  age: '))

def info_age_name(name, age):
    res = name, age
    return res
name_age = info_age_name(name, age)
print(name_age)