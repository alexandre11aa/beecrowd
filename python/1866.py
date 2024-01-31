#### Dois amigos pedem ao atendente de uma lanchonete propor um desafio, de modo que quem acertasse mais, não precisaria pagar a c
#### onta. Então foi proposto o seguinte: Dado o seguinte somatório abaixo, informar o resultado, com uma quantidade de termos nom
#### esmo: S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ... Escreva um programa que, dada uma quantidade de termos, informar o resultado do s
#### oatório acima. Um número inteiro C será informado, que será a quantidade de casos de teste. Cada caso de teste inicia com umn
#### úmero inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de termos da soma. Para cada caso de teste imprima um número S, que éo
#### resultado da soma dos N termos da expressão. Q:1866

nmr = int(input())

for i in range(nmr):
	ip = int(input())
	
	if ip % 2 == 0:
		print(0)
	else:
		print(1)
