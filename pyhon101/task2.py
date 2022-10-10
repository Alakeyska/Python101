# Напишите программу, которая запрашивала бы у пользователя- его имя (например, "What is your name?")- возраст ("How old are you?")- место жительства ("Where are you live?") После этого выводила бы три строки: "This is имя" "It is возраст" "(S)he lives in место_жительства" Вместо имя, возраст, место_жительства должны быть данные, введенные пользователем.


name = input('Enter name: ')
age = input('Enter age: ')
location = input('Enter location: ')

str = "This is %s. It is %s. He lives in %s." % (name, age, location)
print(str)