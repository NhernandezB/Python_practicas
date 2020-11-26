'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5$ y si es mayor de 18 años, 10$.
'''
print("PAGOS AUTOMÁTICOS")
print("Los precios son: ")
print("Cliente con 4 años entra gratis")
print("Cliente entre 4 años y 18 años 5$")
print("Cliente mayor a 18 añor 10$")
print("\n")

edad_cliente = int(input("Por favor introduzca su edad: "))

if (edad_cliente <= 4):
	print("Entrada Gratis :D")
elif(edad_cliente >=4 and edad_cliente < 18):
	print("Pagar 5$")
else:
	print("Pagar 10$")
