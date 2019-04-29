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

#show list

''''for element in lista:
    print(element)'''

# to delete to end
print(lista)
lista.pop()
print(lista)

# join list
listaB = ['lista2',False,365] 
lista_num = [25,36,15,1,3,7,23]
lista.extend(listaB)
print(lista)

#delete elements in list
del lista[5]
#other mode to delete ////
# lista.remove(5)
print(lista)
lista_num.sort()

# lista_num.sort(reverse= True)
print(lista_num)


# index negative 

print(lista_num[-2])