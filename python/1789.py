#### A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que várias pessoas dediquem suas vidas tenta
#### ndo capturar lesmas velozes, e treina-las para faturar milhões em corridas pelo mundo. Porém a tarefa de capturar lesmas velo
#### zes não é uma tarefa muito fácil, pois praticamente todas as lesmas são muito lentas. Cada lesma é classificada em um nível d
#### ependendo de sua velocidade: Nível 1: Se a velocidade é menor que 10 cm/h . Nível 2: Se a velocidade é maior ou igual a 10 cm
#### /h e menor que 20 cm/h . Nível 3: Se a velocidade é maior ou igual a 20 cm/h . Sua tarefa é identificar qual nível de velocid
#### ade da lesma mais veloz de um grupo de lesmas. A entrada consiste de múltiplos casos de teste, e cada um consiste em duas lin
#### has: A primeira linha contém um inteiro L (1 ≤ L ≤ 500) representando o número de lesmas do grupo, e a segunda linha contém L
#### inteiros Vi (1 ≤ Vi ≤ 50) representando as velocidades de cada lesma do grupo. A entrada termina com o fim do arquivo (EOF).P
#### ara cada caso de teste, imprima uma única linha indicando o nível de velocidade da lesma mais veloz do grupo. Q:1789

while True:
	try:
		con = int(input())
		cor = list(map(int,input().split()))
		rap = cor[0]

		for c in range(con):
			if cor[c] > rap:
				rap = cor[c]
		
		if rap < 10:
			print(1)
		elif 10 <= rap < 20:
			print(2)
		else:
			print(3)

	except EOFError:
		break
