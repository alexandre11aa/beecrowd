### Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltim
### o, etc., até trocar o 10º com o 11º. Mostre o vetor modificado. A entrada contém 20 valores inteiros, positivos ou negativos.P
### ara cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição. Q:1175

v = []

for i in range(20):
	nmr = float(input())
	v.append(nmr)

cont = 0

for j in range(20-1,-1,-1):
	print("N[%.f] = %.f" % (cont,v[j]))
	cont += 1
