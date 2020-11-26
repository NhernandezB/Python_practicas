#Programa que simule 100 tiradas de dos dados y despliegue en 
#cuanto a la suma
#de los dos dados sea 10
import random
dado_1 = [1,2,3,4,5,6]
dado_2 = [1,2,3,4,5,6]

for x in range(1,100):
	a = random.choice(dado_1)
	b = random.choice(dado_2)
	c = a+b
	if  (c == 10):
		print("Tirada " + str(x) + ":"+" Dado 1: "+str(a)  + " Dado 2: "+ str(b))
		print("\n")