#### Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez, ele inventou um jogo chamado "Jogo do Operador"
#### , em que ele cria expressões básicas e cada jogador deve escolher uma expressão e preencher a lacuna com o operador correto pa
#### ra validá-la. Os jogadores poderão escolher operadores de somente três tipos: adição, subtração e multiplicação. Porém, se o j
#### ogador achar que não há operador entre os três tipos que valide a expressão, poderá responder Impossível. Sua tarefa é simples
#### : dadas as expressões e as respostas dos jogadores, determinar os jogadores que não passarão para a outra fase do jogo. A entr
#### ada é composta por um inteiro T (2 ≤ T ≤ 50) que indica a quantidade de expressões e de jogadores. Cada caso de teste é compos
#### to por T expressões na forma "X Y=Z", indicando que X operador Y (0 ≤ X, Y ≤ 103) é igual a Z (-103 ≤ Z ≤ 106), seguido de T j
#### ogadores e suas respectivas respostas na forma "N E R", sendo N o nome do jogador (até 50 caracteres e sem espaços), E o índic
#### e da expressão escolhida (1 ≤ E ≤ T) e R a resposta (+, -, * ou I, indicando Impossível). A entrada termina com EOF (fim de ar
#### quivo). Para cada caso de teste, se todos os jogadores passarem, imprima "You Shall All Pass!"; se nenhum jogador passar, impr
#### ima "None Shall Pass!"; caso contrário, imprima, em ordem lexicográfica e entre espaços, o nome dos jogadores que erraram a re
#### sposta e, desta forma, não passarão para a próxima fase do jogo. Q:2493

while True:
	try:
		jgs = int(input())
		
		op_c, op_j, indc, noms, jg_e = [[0],[0],[0],[],[]]

		for i in range(jgs):
			qst = input()

			x0 = qst.split()
			x1 = x0[0] + "=" + x0[1]
			x2 = x1.split("=")

			if int(x2[0]) + int(x2[1]) == int(x2[2]):
				op_c.append("+")
			elif int(x2[0]) - int(x2[1]) == int(x2[2]):
				op_c.append("-")
			elif int(x2[0]) * int(x2[1]) == int(x2[2]):
				op_c.append("*")
			else:
				op_c.append("I")

		for i in range(jgs):
			jgd = input()

			x = jgd.split()

			if x[2] == "+":
				op_j.append("+")
			elif x[2] == "-":
				op_j.append("-")
			elif x[2] == "*":
				op_j.append("*")
			else:
				op_j.append("I")

			indc.append(int(x[1]))
	
			noms.append(x[0])
		
		for i in range(jgs):
			if op_j[i + 1] != op_c[indc[i + 1]]:
				jg_e.append(noms[i])
				
		if len(jg_e) == len(noms):
			print("None Shall Pass!")
		elif len(jg_e) == 0:
			print("You Shall All Pass!")
		else:
			jg_e = sorted(jg_e)

			p = jg_e[0]

			for i in range(1,len(jg_e)):
				p += " " + jg_e[i]

			print(p)

	except:
		break
