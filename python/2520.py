#### Analógimôn Go! é um jogo bastante popular. Em sua jornada, o jogador percorre diversas cidades capturando pequenos monstrinhos
#### virtuais, chamados analógimôns. Você acabou de chegar em uma cidade que contém o último analógimôn que falta para sua coleção!
#### A cidade pode ser descrita como um grid de N linhas e M colunas. Você está em uma dada posição da cidade, enquanto o último an
#### alógimôn está em outra posição da mesma cidade. A cada segundo, você pode se mover (exatamente) uma posição ao norte, ao sul,a
#### leste ou a oeste. Considerando que o analógimôn não se move, sua tarefa é determinar o menor tempo necessário para ir até a po
#### sição do monstrinho. A figura abaixo descreve o exemplo da entrada, e apresenta um caminho percorrido em 5 segundos. Outros ca
#### minhos percorridos no mesmo tempo são possíveis, mas não há outro caminho que pode ser percorrido em um tempo menor. A entrada
#### contém vários casos de teste. A primeira linha de cada caso contém dois inteiros N e M (2 ≤ N, M ≤ 100), o número de linhas ed
#### e colunas na cidade, respectivamente. As próximas N linhas contém M inteiros cada, descrevendo a cidade. O inteiro 0 indica um
#### a posição em branco; o inteiro 1 indica a sua posição na cidade; o inteiro 2 indica a posição do analógimôn na cidade. É garan
#### tido que haverá exatamente um inteiro 1 e exatamente um inteiro 2 na descrição da cidade, e que os demais inteiros serão iguai
#### s a 0. A entrada termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma linha contendo o menor tempo necessári
#### o para ir até o monstrinho, em segundos. Q:2520

while True:
	try:
		lc = list(map(int,input().split()))

		m = []

		for i in range(lc[0]):
			m.append(list(map(int,input().split())))

		pok, ash, con = [[],[],0]

		for l in range(lc[0]):
			for c in range(lc[1]):
				if m[l][c] == 2:
					pok.append(l)
					pok.append(c)
				elif m[l][c] == 1:
					ash.append(l)
					ash.append(c)

		if pok[0] < ash[0]:
			while True:
				if ash[0] == pok[0]:
					break

				ash[0] -= 1
				con += 1
		elif pok[0] > ash[0]:
			while True:
				if ash[0] == pok[0]:
					break

				ash[0] += 1
				con += 1

		if pok[1] < ash[1]:
			while True:
				if ash[1] == pok[1]:
					break
	
				ash[1] -= 1
				con += 1
		elif pok[1] > ash[1]:
			while True:
				if ash[1] == pok[1]:
					break

				ash[1] += 1
				con += 1

		print(con)

	except:
		break
