from msilib.schema import tables

my_dict = {'Denis': 1987, 'Alexa': 1985, 'Ivan': 1980 }
print(my_dict)
print(my_dict['Alexa'] )
my_dict['Ivan'] = 2000
print(my_dict)
my_dict.update({'Sergei':2001,'Alexsey':2005})
print(my_dict)
del my_dict['Sergei']
print(my_dict)
my_set = {1,'apple',42,111.54,1,42}
print(my_set)
my_set.add('tables')
my_set.add(25)
print(my_set)
my_set.remove('apple')
print(my_set)

