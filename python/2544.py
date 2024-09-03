#### O Kage Bunshin no Jutsu (ou a "técnica dos clones de sombra", para os lusofalantes) é uma técnica milenar bastante utilizada e
#### m batalhas ninja. Quando utilizada, a técnica cria uma cópia idêntica de seu usuário. Desta forma, se um dado ninja usa a técn
#### ica, passam a existir dois destes ninjas (o original e a cópia). A técnica sempre é executada por todos os ninjas existentes n
#### o momento. Desta forma, se a técnica for utilizada novamente, passam a existir quatro ninjas idênticos ao original (os dois an
#### teriores e mais duas cópias), e assim por diante. Há N cópias de um dado ninja (incluindo o original). Sua tarefa é determinar
#### quantas vezes a técnica foi utilizada. A entrada contém vários casos de teste. Cada caso contém uma linha com o número N (1 ≤N
#### ≤ 106). É garantido que o valor de N é tal que é possível obter exatamente N cópias de um ninja utilizando a técnica (incluind
#### o o original). A entrada termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma linha contendo o número de vez
#### es que a técnica foi utilizada. Q:2544

while True:
	try:
		nmr = int(input())

		s = 0
		n = 1
		
		while True:

			if n == nmr:
				break

			n *= 2
			s += 1

		print(s)

	except:
		break
