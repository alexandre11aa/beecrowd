#### Certo dia, os irmãos Little Chitão e Xor Or Oh, exímios digitadores, fizeram um desafio, para ver quem era o melhor na digitaç
#### ão. Para isto, conseguiram um computador que não processa teclas pressionadas, ou seja, se for para digitar a mesma letra duas
#### vezes seguidas, precisa pressionar a tecla duas vezes, visto que, pressionar a tecla por mais tempo, não adianta. Também medir
#### am o tempo de uma tecla pressionada, que foi de, exatamente, um centésimo de segundo. O desafio seria quem digitasse a palavra
#### “galopeira”, formada por mais letras e, mas ambos eram muito bons, e chegava num ponto que não era possível contar quantas let
#### ras haviam sido digitadas. Então, pediram a sua ajuda para escrever um programa que verifique a palavra digitada e veja quanto
#### tempo foi gasto para a digitação. Escreva um programa que, dada uma palavra digitada, informe quanto tempo foi gasto para serd
#### igitada. Um número inteiro C será informado, que será a quantidade de casos de teste. Cada caso tem uma palavra, de, no mínimo
#### , 9 e, no máximo 10000 letras. Para cada caso de teste, imprima um número T, que é o tempo gasto, em segundos, para digitar ap
#### alavra do respectivo caso de teste, com aproximação de duas casas decimais. Q:2147

qtd = int(input())

for i in range(qtd):
	g = input()

	print("%.2f" % (len(g) * 0.01))
