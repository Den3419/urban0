immutable_var = ("строка", 42,True,[1,2,3,])
print(immutable_var)
immutable_var[0] = "Новая строка"  # кортеж нельзя изменить
mutable_list = ["строка",45,True,[1, 2, 3]]
mutable_list[0] = "Новая_строка"
print(mutable_list)