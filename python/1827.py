#### Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchi
#### da da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchi
#### da com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo. Obs: o qu
#### adrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em ze
#### ro (0). A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor int
#### eiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz. Para cada caso de teste, imprima a matriz correspondente conforme o exe
#### mplo abaixo. Após cada caso de teste, imprima uma linha em branco. Q:1827

while True:
	try:
		nmr = int(input())
		m = []

		for l in range(nmr):
			m.append([])
			for c in range(nmr):
				m[l].append(0)

		uns = 3
		con = True

		while con == True:
			if nmr/uns <= 3:
				con = False
			else:
				uns += 2

		nx = int((nmr - uns)/2)

		for l in range(nx,uns+nx):
			for c in range(nx,uns+nx):
				m[l][c] = 1

		m[int((nmr - 1)/2)][int((nmr - 1)/2)] = 4

		c1 = 0
		c2 = nmr - 1

		for l in range(nx):
			m[l][c1] = 2
			c1 += 1

		for l in range(nx):
			m[l][c2] = 3
			c2 -= 1

		c3 = c1 - 1
		c4 = c2 + 1

		for l in range(nx+uns,nmr):
			m[l][c3] = 3
			c3 -= 1

		for l in range(nx+uns,nmr):
			m[l][c4] = 2
			c4 += 1
		
		for l in range(nmr):
			pri = ""
			for c in range(nmr):
				m[l][c] = str(m[l][c])
				pri += m[l][c]
			print(pri)
		print("")

	except EOFError:
		break
