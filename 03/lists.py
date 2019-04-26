#list are mutable
# it's same than tuples 
# 
lista = ['lista',1,25.6,True]
#print(lista)

# to change 
lista[1] = 'nuevo dato'
#print(lista[1])

# add elements to list

lista.append(25)

for element in lista:
    print(element)

# to delete 
print(lista)
lista.pop()
print(lista)