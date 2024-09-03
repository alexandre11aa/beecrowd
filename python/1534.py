#### Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido. A entrada contém váriosc
#### asos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (
#### linhas e colunas) de uma matriz que deve ser impressa. Para cada N lido, apresente a saída conforme o exemplo fornecido. Q:15
#### 34

while True:
	try:
		nmr = int(input())

		m = []

		if nmr % 2 == 0:
			con = int(nmr/2)
		else:
    			con = int((nmr + 1)/2)
    
		for l in range(int(nmr)):
    			m.append([])
    			for c in range(int(nmr)):
        			m[l].append(3)
    
		c1 = 0
		c2 = nmr - 1

		for l in range(con):
			m[l][c1] = 1
			c1 += 1

		for l in range(con):
			m[l][c2] = 2
			c2 -= 1

		c3 = c2
		c4 = c1

		for l in range(con,nmr):
			m[l][c3] = 2
			c3 -= 1
    
		for l in range(con,nmr):
			m[l][c4] = 1
			c4 += 1

		for l in range(nmr):
			pri = ""
			for c in range(nmr):
				pri += "%d" % m[l][c]
			print(pri)

	except EOFError:
		break
