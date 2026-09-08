print("Clasificador de edades")
name = input("ingrese su nombre : ")
last_name = input ("ingresa tu apellido :")
age = int(input ("ingresa tu edad "))
if 0 <= age <= 2 :
    print("category: bebe ")
elif 3 <=  age <= 11 :
    print("category : niño ")
elif 12 <= age <= 13 :
    print ("category : preadolescente ")
elif 14 <= age <= 17 :
    print("category : adolescente ")
elif 18 <=  age <= 35 :
    print("category : adulto joven")
elif 36 <= age <= 64 :
    print("category : adulto")
else: 
    print("category : adulto mayor")