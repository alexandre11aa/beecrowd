#### No crepúsculo, a cidade de Portland fica cheia de vampiros e lobisomens. Entretanto, nenhum deles quer ser visto enquanto pass
#### eiam pelo centro. Vão ser instaladas câmeras de vigilância em cada esquina do centro de Portland. A cada mês, um mapa atualiza
#### do com as câmeras já em funcionamento é disponibilizado no site da prefeitura. Uma quadra é considerada segura se existem câme
#### ras em, pelo menos, duas de suas quatro esquinas. No centro de Portland todas as quadras são quadrados de mesmo tamanho. Sua t
#### arefa é, dado o mapa das câmeras em funcionamento nas esquinas, indicar o status de todas as quadras do centro. A primeira lin
#### ha da entrada tem um inteiro positivo N (1 ≤ N ≤ 100). Nas próximas N+1 linhas, existem N+1 números, que indicam, para cada es
#### quina, a presença ou ausência de uma câmera de vigilância em funcionamento. O número 1 indica que existe uma câmera funcionand
#### o na esquina, enquanto o número zero indica que não há câmera funcionando. A saída é dada em N linhas. Cada linha tem N caract
#### eres, indicando se a quadra correspondente é segura ou insegura. Se uma quadra é segura, mostre o caractere S; se não é segura
#### , mostre o caractere U. Q:2168

qud = int(input())

cdd = []

for l in range(qud + 1):
	cdd.append(list(map(int,input().split())))

mat = []

for l in range(qud + 1):
	for c in range(qud + 1):
		if l < qud and c < qud:
			if (cdd[l][c] + cdd[l][c+1] + cdd[l+1][c] + cdd[l+1][c+1]) >= 2:
				mat.append("S")
			else:
				mat.append("U")

c = 0

for l in range(qud):
	p = ""
	for i in range(qud):
		p += mat[c]
		c += 1

	print(p)
