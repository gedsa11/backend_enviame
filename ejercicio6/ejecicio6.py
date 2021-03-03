import random

km = random.randint(0, 2000)
km_t = int(km/100)

print("total de km: ",km)

a, b = 0, 1
for i in range(km_t):
	a, b = b, a+b

print("Tiempo de entrega : {} día(s).".format(a))

