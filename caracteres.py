'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la 
contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
n = 0
contraseña = input("Introduzca la contraseña: ")
contraseñag = "Hola"

while n  < 10:
	
	if (contraseña == contraseñag):
		print("Bienvenido")
	else:
		print("Contraseña incorrecta intentelo de nuevo")

	n = n+1