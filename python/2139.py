#### Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando ganha presente dos pais e dos avós. Esse ano,
#### seu pai lhe prometeu um PS4, mas somente se Pedrinho conseguir resolver alguns desafios ao longo do ano, sendo um deles, escre
#### ver um programa que calcule quantos dias faltam para o Natal. Entretanto, Pedrinho tem somente 9 anos e não tem noção alguma d
#### e programação, mas sabe que você, primo dele, mexe com "coisas de computador", e dessa forma, pediu para você escrever o progr
#### ama para ele. Não somente isso, mas prometeu que deixaria você jogar todo final de semana e por quanto tempo quiser! A entrada
#### é composta por vários casos de teste. Cada linha contém o mês e o dia do ano de 2016 (ano bissexto). A entrada termina com fim
#### de arquivo. Se for Natal, imprima "E natal!"; se faltar somente um dia, imprima "E vespera de natal!"; se já passou, imprima "
#### Ja passou!". Caso contrário, imprima "Faltam X dias para o natal!", sendo X o número de dias que faltam para o Natal. Q:2139

while True:
	try:
		m, d = map(int,input().split())

		l, s, f = [[31,29,31,30,31,30,31,31,30,31,30,31],0,0]

		for i in range(m):
			s += l[i]

		for i in range(m,12):
			f += l[i]

		natal = s - (l[m - 1] - d)
		falta = f + (l[m - 1] - d - 6)

		if natal > 360:
			print("Ja passou!")
		elif natal == 359:
			print("E vespera de natal!")
		elif natal == 360:
			print("E natal!")
		else:
			print("Faltam %.i dias para o natal!" % falta)

	except:
		break
