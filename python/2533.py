#### A Googlbook é uma famosa empresa de tecnologia mundial que acabou de abrir uma filial na sua cidade! Além disso, a Googlbook t
#### ambém acabou de abrir as inscrições do processo seletivo para uma vaga de estágio na empresa! Para se inscrever no processo se
#### letivo, você deve enviar algumas informações para a empresa, que irá usá-las para decidir quem será contemplado com a vaga. Vo
#### cê já enviou todas as informações necessárias, exceto uma: seu IRA (Índice de Rendimento Acadêmico). Para piorar, o Portão doA
#### luno, sistema que disponibiliza o histórico com IRA, está fora do ar! Felizmente, você lembra de suas notas em todas as M disc
#### iplinas que cursou, além de suas respectivas cargas horárias. Você também lembra que o IRA é calculado da seguinte maneira: ,o
#### nde N1, N2, ..., NM são suas notas em cada disciplina, e C1, C2, ..., CM são as cargas horárias das discplinas respectivas. Da
#### da a nota obtida e a carga horária de cada disciplina, determine seu IRA para poder enviá-lo para a Googlbook o mais breve pos
#### sível! A entrada contém vários casos de teste. A primeira linha de cada caso contém o inteiro M (1 ≤ M ≤ 40), o número de disc
#### iplinas cursadas. As próximas M linhas descrevem uma disciplina cada. Cada linha contém dois inteiros Ni e Ci (0 ≤ Ni ≤ 100, 3
#### 0 ≤ Ci ≤ 120), indicando a nota obtida na disciplina e a carga horária da mesma, respectivamente. A entrada termina com fim-de
#### -arquivo (EOF). Para cada caso de teste, imprima uma linha contendo o valor do seu IRA. Arredonde e imprima a resposta com exa
#### tamente 4 casas decimais. Q:2533

while True:
	try:
		qntd = int(input())
		
		dvs, dvd = [0,0]

		for i in range(qntd):
			n, c = map(int,input().split())

			dvs += (c * n)
			dvd += c

		print("%.4f" % (dvs/(dvd * 100)))

	except:
		break
