
#### Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caract
#### ere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e m
#### ostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o casod
#### a entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados na operação. A primeiral
#### inha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação. A segunda linha de ent
#### rada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os
#### elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz. Imprima o resultado solicitado (a soma ou
#### média), com 1 casa após o ponto decimal. Q:1182

cx = int(input())

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

for l in range(12):
	sm += matriz[l][cx]

if decisao == "M":
	sm /= 12

print("%.1f" % sm)
