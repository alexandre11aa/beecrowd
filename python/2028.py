#### Hyam é um menino que adora sequências. Ele anda descobrindo sequências interessantes que nem mesmo Fibonacci imaginaria. Certo
#### dia, Hyam percebeu que dado um número N, ele poderia fazer uma sequência do tipo 0 1 2 2 3 3 3 4 4 4 4 ... N N N ... N. No ent
#### anto, Hyam percebeu que cada valor que aumentava no número da sequência, a quantidade total de números da sequência aumentavas
#### emelhantemente à um crescimento fatorial, neste caso, ao invés de multiplicar, soma-se o número total de números da sequênciac
#### om o valor do próximo número da sequência. Por exemplo, se N = 2. A sequência correta seria 0 1 2 2, obtendo-se 4 digitos. Ago
#### ra, se N = 3, o próximo número da sequência tem valor 3, então a quantidade total de número da sequência seria a quantidade de
#### números com N = 2, que é 4, mais o valor do próximo número da sequência, neste caso 3, obtendo-se 7, já que a sequência corret
#### a para N = 3 é 0 1 2 2 3 3 3. Sua tarefa é fazer um algoritmo que dado um número inteiro N, tenha como resposta a quantidade t
#### otal de números dessa sequência e logo abaixo a sequência completa. A entrada é composta de vários casos de testes. Cada casoé
#### composto por um inteiro N (0<=N<=200) que indica o valor dos últimos N números da sequência. A entrada termina com final de ar
#### quivo (EOF). A saida é no formato Caso X: N numeros onde X é a ordem do número de casos e N é a quantidade de numeros que cont
#### ém na sequência completa, na próxima linha a sequência de números com um espaço entre eles. É pedido que deixe uma linha em br
#### anco após cada caso. Q:2028

c = 1

while True:
	try:

		nmr = int(input())

		nmr += 1
		p = "0"
		n = 0

		for i in range(nmr):
			if i != 0:
				for l in range(i):
					if i != l:
						p += " " + str(i)
						n += 1
					else:
						p += str(i)
						n += 1

		if len(p) == 1:
			print("Caso %.i: %.i numero" % (c,n + 1))
			print(p)
			print("")
		else:
			print("Caso %.i: %.i numeros" % (c,n + 1))
			print(p)
			print("")
		
		c += 1

	except EOFError:
		break
