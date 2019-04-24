#tuplas

tupla = (1,2,3,4,5) # tupla  of integers
tupla2= ("nombre","apellido","direccion") #tupla of strings
tupla3 = ('cadena',1,True,2.5) # tupla mixed
#print(tupla3)
#print(tupla3[0])
#tupla3[0] =  1   tuples don't support asignaments
user = ('ariel','ariel@correo.com',23,1.56)
for data in user:
    print(data)

def send_user ():
    name = "Ariel"
    last_name = 'Monterroso'
    email = 'ariel@correo.com'
    age = 23
    return (name,email,age,last_name)

def get_user(user):
    print(user[0],user[3])

get_user(send_user())
