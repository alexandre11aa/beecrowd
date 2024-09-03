#### Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere m
#### aiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre
#### a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da ent
#### rada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação. A primeira linhad
#### e entrada contem um número L (0 ≤ L ≤ 11) indicando a linha que será considerada para operação. A segunda linha de entrada co
#### ntém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elemen
#### tos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz, sendo que a mesma é preenchida linha por linha,
#### da linha 0 até a linha 11, sempre da esquerda para a direita. Imprima o resultado solicitado (a soma ou média), com 1 casa ap
#### ós o ponto decimal. Q:1181

lx = int(input())

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

for c in range(12):
	sm += matriz[lx][c]

if decisao == "M":
	sm /= 12

print("%.1f" % sm)
