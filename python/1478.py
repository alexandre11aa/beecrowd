#### Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a ma
#### triz de acordo com o exemplo abaixo. A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das
#### matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0). Para cada inteiro da entra
#### da imprima a matriz correspondente, de acordo com o exemplo. (os valores das matrizes devem ser formatados em um campo de tam
#### anho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaçose
#### m branco. Após a impressão de cada matriz deve ser deixada uma linha em branco. Q:1478

while True:
	nmr = int(input())

	if nmr <= 0:
		break
	else:
		m = []
		con = 1
        
		for l in range(nmr):
			m.append([])
			con1 = con
			con2 = 1
			for c in range(nmr):
				if con1 <= con and con1 != 1:
					m[l].append(con1)
					con1 -= 1
				else:
					m[l].append(con2)
					con2 += 1
                    
			con += 1
                   	
		for l in range(nmr):
			pri = ""
			for c in range(nmr):
				pri += " %3d" % m[l][c]
			print(pri[1:])
		print("")
