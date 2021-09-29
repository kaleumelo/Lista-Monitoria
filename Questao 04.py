i = 1
lista = []
notas_maiores = []
notas_menores = []
print('Digite as notas desse semestre. Ao final, digite "-1"')
while(1):
	notas = int(input('Nota ' + str(i) + ': '))
	i += 1
	if(notas == -1):
		print('Acabaram as notas!')
		break
	else:
		lista.append(notas)
media = (sum(lista)/len(lista))
print(len(lista))
print(lista)
lista.reverse()

for i in range(len(lista)):
    print(lista[i])

for i in range(len(lista)):
	if(lista[i] > media):
		notas_maiores.append(lista[i])
print(notas_maiores)

for i in range(len(lista)):
	if(lista[i] < 7):
		notas_menores.append(lista[i])
print(notas_menores)


print(sum(lista))
print(media)