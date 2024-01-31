#### Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mos
#### tre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal Secundária da matriz, conforme ilus
#### trado abaixo (área verde). A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operaç
#### ão (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõema
#### matriz. Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal. Q:1186

decisao = input()

while decisao != "S" and decisao != "M":
	decisao = input()

matriz = []

c1 = input()

if len(c1) > 11:
	matriz.append(list(map(float,c1.split())))
	for l in range(1,12):
		matriz.append(list(map(float,input().split())))

else:
	c1 = float(c1)
	matriz.append([])
	matriz[0].append(c1)
	for l in range(1,12):
		matriz[0].append(float(input()))
	for l in range(1,12):
		matriz.append([])
		for c in range(12):
			matriz[l].append(float(input()))

sm = 0
ll = 12

for l in range(12):
	for c in range(ll,12):
		sm += matriz[l][c]
	ll -= 1


if decisao == "M":
	sm /= 66

print("%.1f" % sm)
