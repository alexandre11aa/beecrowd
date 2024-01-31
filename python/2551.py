#### A grande Maratona de Rua de Curitiba irá ocorrer nos próximos dias! Vários atletas estão treinando há dias para o grande dia d
#### a corrida. Flávio é um dos atletas que está treinando diariamente para se sair bem na corrida. Ele tem corrido todas as manhãs
#### nas pistas próximas de sua casa. Os treinos do garoto são monitorados por um aplicativo em seu celular. Após cada treino, Fláv
#### io sabe tanto a duração do treino quanto a distância total percorrida. Com essas informações, ele consegue determinar a veloci
#### dade média obtida em cada treino. Flávio está muito preocupado com a evolução de seu desempenho nos treinos, e em particular c
#### om seu recorde de velocidade média. Tal recorde é batido em um dado treino quando a velocidade média para este treino é maiorq
#### ue todas as velocidades médias obtidas nos treinos anteriores. Ajude Flávio a determinar em quais treinos ele conseguiu baters
#### eu recorde. A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 30), o número d
#### e treinos feitos. Considere que os treinos foram feitos nos dias 1, 2,...,N. As próximas N linhas descrevem os treinos. A linh
#### a i (1 ≤ i ≤ N) contém dois inteiros Ti e Di (1 ≤ Ti, Di ≤ 100), indicando, respectivamente, a duração do treino (em minutos)e
#### a distância percorrida no treino (em quilômetros). A entrada termina com fim-de-arquivo (EOF). Para cada caso de teste, imprim
#### a uma lista de inteiros indicando os dias nos quais o recorde foi batido. Cada dia deve ser impresso em uma linha. Imprima osd
#### ias em ordem crescente. Note que o dia 1 sempre deve ser impresso. Q:2551

while True:
	try:
		dias, m_re, re, dia = [[],[],0,0]

		qtdd = int(input())
		
		for i in range(qtdd):
			dias.append(list(map(int,input().split())))

		for l in range(qtdd):
			dia += 1

			div = dias[l][1] / dias[l][0]

			if div > re:
				re = div
				m_re.append(dia)

		for i in range(len(m_re)):
			print(m_re[i])
				
	except:
		break
