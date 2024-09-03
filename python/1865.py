#### Odin criou para Thor a mais fiel e poderosa arma possível, o martelo Mjölnir. Feito de um minério místico especial chamado Ur
#### u e forjado no coração de uma estrela pelos Deuses ferreiros de Asgard, Brokk e Eitri, os lendários ferreiros. Um dia, Thor d
#### esafiou seus amigos para ver quem conseguia levantar o Mjölnir. Escreva um programa que, dado um nome, e a força, em Newtons,
#### aplicado ao tentar levantar o Mjölnir, informar se a pessoa conseguiu ou não levantá-lo. Um número inteiro C será informado,q
#### ue será a quantidade de casos de teste. Cada caso de teste inicia com uma palavra, que é o primeiro nome de quem está tentand
#### o levantar o Mjölnir, e um inteiro N (1 ≤ N ≤ 25000), indicando a força aplicada para cima, em Newtons, ao puxar o martelo, d
#### e modo a tentar levantá-lo. Para cada caso de teste imprima um caractere ‘Y’, caso a pessoa tenha conseguido levantar , ou ‘N
#### ’, caso não tenha conseguido. Q:1865

nmr = int(input())

for i in range(nmr):
	p = list(input().split())

	if p[0] == "Thor":
		print("Y")
	else:
		print("N")
