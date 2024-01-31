
#### Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a mat
#### riz de acordo com o exemplo abaixo. A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens dasm
#### atrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0). Para cada inteiro da entrad
#### a imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de taman
#### ho T justificados à direita e separados por espaço, onde T é igual ao número de dígitos do maior número da matriz. Após o últ
#### imo caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada umal
#### inha em branco. Q:1557

while True:
	nmr = int(input())

	if nmr == 0:
		break

	else:
		m = []
		v = 1

		for l in range(nmr):
			m.append([])
			u = v
			for c in range(nmr):
				m[l].append(u)
				u *= 2
			v *= 2

		f = len(str(m[nmr-1][nmr-1]))
		
		for l in range(nmr):
			for c in range(nmr):
				m[l][c] = str(m[l][c])
				while len(m[l][c]) < f:
					m[l][c] = " " + m[l][c]

			print((" ").join(m[l]))
		print("")
