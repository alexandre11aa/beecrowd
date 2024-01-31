#### Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesmao
#### rdem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência con
#### tígua do segundo. A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cad
#### a entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032). Para
#### cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mai
#### s de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subseq
#### uencia". Mostre o resultado conforme o exemplo de saída. Q:2126

co = 0

while True:
	try:
		nmr = input()
		seq = input()

		co += 1 
		c0 = 0
		po = 0

		for t in range(len(seq)):
			c1 = t
			c2 = 0

			if seq[t] == nmr[0]:
				for n in range(len(nmr)):
					if c1 >= len(seq):
						break

					if nmr[n] == seq[c1]:
						c2 += 1
					c1 += 1
				
			if c2 == len(nmr):
				c0 += 1
				po = t + 1
		
		if c0 != 0:
			print("Caso #%.i:" % co)
			print("Qtd.Subsequencias:", c0)
			print("Pos:", po)
			print("")
		else:
			print("Caso #%.i:" % co)
			print("Nao existe subsequencia")
			print("")

	except EOFError:
		break
