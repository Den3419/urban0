user_input = input("Введите_строку")
my_string = user_input
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
my_string_no_spaces = ''.join(my_string.split() )
print(my_string_no_spaces)
print(my_string[0])
print(my_string[-1])