#### Domingo é dia de feira. Logo de manhã muitas pessoas se deslocam para o polo de lazer da Parangaba, onde acontece uma feira, c
#### onhecida por ser a maior da cidade. Na feira da Parangaba você pode encontrar de tudo. Todos os domingos, Bino faz compras naf
#### eira. Ele sempre marca com seu amigo Cino de se encontrarem no terminal de ônibus da Parangaba às 8h, para irem juntos comprar
#### na feira. Porém, muitas vezes Bino acorda muito tarde e se atrasa para o encontro com seu amigo. Sabendo que Bino leva de 30 a
#### 60 minutos para chegar ao terminal. Diga o atraso máximo de Bino. A entrada consiste em múltiplos casos teste. Cada caso de te
#### se contém uma única linha contendo um horário H (5:00 ≤ H ≤ 9:00) que Bino acordou. A entrada termina com final de arquivo (EO
#### F). Para cada caso de teste, imprima "Atraso maximo: X" (sem aspas), X indica o atraso maximo (em minutos) de Bino no encontro
#### com Cino. Q:2003

while True:
	try:
		tem = input()

		hra = tem[0]
		min = tem[2] + tem[3]

		if int(hra) == 7:
			print("Atraso maximo:",int(min))
		elif int(hra) == 8:
			print("Atraso maximo:",60 + int(min))
		elif int(hra) == 9:
			print("Atraso maximo:",120 + int(min))
		else:
			print("Atraso maximo: 0")

	except EOFError:
		break
