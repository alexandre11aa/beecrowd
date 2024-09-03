### Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguidam
### ostre o vetor X. A entrada contém 10 valores inteiros, podendo ser positivos ou negativos. Para cada posição do vetor, escreva
### "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição. Q:1172

v = []

for i in range(10):
	nmr = int(input())
	if nmr > 0:
		v.append(nmr)
		print("X[%.f] = %.f" % (i,v[i]))
	else:
		v.append(1)
		print("X[%.f] = %.f" % (i,v[i]))
