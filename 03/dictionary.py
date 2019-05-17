

autors = {'libro 1':'Predro Vasquez','libro 2':'Carlos Miguel'}
#print(autors['libro 2'])

# for to print values 

print(autors.values())

# for to print keys

print(autors.keys())

#for autor in autors:
   # print(autor)
                       #tuple          tuple                     list 
diccionnario = {'a':(1,True,'hola'),'b':(22.25,'mundo',False),'c':[112,25.5,'doki']}

# clean dictionary

#autors.clear()

# copy dictionaries 

newdictionary = autors.copy()
print(newdictionary)

print(newdictionary.get('libro 1'))

#update dictionary

user = {'name':'Jose','last_name':'Hernandez','Age':25,'City':'Guatemala'}
new_name = {'name':'Antonio','Age':22}

user.update(new_name)
print(user)