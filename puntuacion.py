'''
Escribir un programa que lea la puntuación del usuario
e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.
'''
puntos = float(input("Introduzca los puntos obtenidos: "))
pago = 2400
if(puntos == 0.0):
	print("Su nivel es inaceptable, su pago es de: ",str(pago*puntos))
elif(puntos == 0.4):
	print("Su nivel es aceptable, su pago es de: ",str(pago*puntos))
elif(puntos >= 0.6):
	print("Su nivel es meritorio,su pago es de: ",str(pago*puntos))