#### Todos os habitantes da Nlogônia estão super animados com a abertura do Ricardo Barreiro World, o mais novo parque de diversões
#### do país. Na TV e no rádio só passam propagandas da montanha-russa do parque, a mais rápida do continente. É nela que todos, de
#### crianças a idosos querem andar. Infelizmente foram impostas algumas restrições no momento da homologação do brinquedo pelo gov
#### erno. Por questões de segurança, há uma altura mínima e uma altura máxima que as pessoam devem ter para poder passear na monta
#### nha-russa. Para o dia da inauguração do parque, todos os convidados realizaram um pré-cadastro no qual indicaram sua altura. P
#### ara reduzir filas e otimizar a operação do parque no primeiro dia, você foi contratado para fazer um programa que dado o númer
#### o de visitantes, altura mínima, altura máxima e as alturas de todos os visitantes, calcule quantas pessoas poderão andar na mo
#### ntanha-russa. A entrada contém vários casos de teste. A primeira linha de cada caso consiste em três inteiros N (1 ≤ N ≤ 100),
#### Amin e Amax (50 ≤ Amin ≤ Amax ≤ 250), o número de visitantes, a altura mínima e máxima em centímetros para andar na montanha-r
#### ussa, respectivamente. As N linhas seguintes contém, cada uma, um número inteiro Ai (50 ≤ Ai ≤ 250), a altura do i-ésimo visit
#### ante, em centímetros. A entrada termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma única linha com o númer
#### o visitantes que podem passear na montanha-russa. Q:2547

while True:
	try:
		qtd, amn, amx = map(int,input().split())
	
		s = 0

		for i in range(qtd):
			alt = int(input())

			if (amx >= alt >= amn):
				s += 1

		print(s)

	except:
		break
