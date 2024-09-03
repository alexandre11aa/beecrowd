#### Em uma determinada competição de saltos ornamentais, cada salto recebe um grau de dificuldade e é avaliado por sete juízes. Ap
#### ós cada salto, os juízes, que não se comunicam uns com os outros, mostram suas notas. Um salto é cotado entre zero e dez ponto
#### s. Depois de apresentadas as notas, a mais alta e a mais baixa são descartadas. O restante é somado e multiplicado pelo grau d
#### e dificuldade do salto, que gira entre 1,2 e 3,8, definido sempre antes do início da apresentação do atleta. O julgamento entã
#### o é feito da seguinte forma: supondo que um saltador tenha sua nota de partida (seu grau de dificuldade de movimento) avaliada
#### em 2,0 e tire notas 6,0, 5,0, 5,0, 5,0, 5,0, 5,0, 4,0 em sua execução. Disso, retira-se a nota mais baixa e a mais alta, o que
#### gera um resultado parcial de 25,0. Então, pega-se a nota de execução e multiplica-a pela nota de partida para se chegar ao res
#### ultado final, que neste exemplo é de 50,0. Seu programa deve apresentar o resultado de uma competição de acordo com estas regr
#### as. A primeira linha de entrada contém o número de competidoresN (0 ≤ N ≤ 100). A seguir são mostrados os nomes de cada um dos
#### competidores seguidos pelo grau de dificuldade dos seus saltos GD (1.2 ≤ GD ≤ 3.8) e, a seguir, na linha seguinte, as 7 notasr
#### ecebidas N1 a N7 (0 ≤ N1 a N7 ≤ 10). A saída deve apresentar o resultado da competição, com o nome dos competidores seguido de
#### seu resultado, na ordem em que os dados foram lidos. Q:2311

qntd = int(input())

for i in range(qntd):
	nome = input()
	dsal = float(input())
	nots = list(map(float,input().split()))

	mair, menr, soma = [0,11,0]

	for i in range(7):
		if nots[i] > mair:
			mair = nots[i]

		if nots[i] < menr:
			menr = nots[i]

	for i in range(7):
		if mair == nots[i]:
			nots.pop(i)
			break
		
	for i in range(6):
		if menr == nots[i]:
			nots.pop(i)
			break

	for i in range(5):
		soma += nots[i]

	print(nome, "%.2f" % (soma * dsal))
