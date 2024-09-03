### Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores r
### eais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que op
### rimeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. O arquivo de entrada contém um valor intei
### ro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor. Para c
### ada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo. Q:1079

cn = 1

ii = int(input())

while cn <= ii:
	ix, iix, iiix = input().split()
	ix = float(ix)
	iix = float(iix)
	iiix = float(iiix)
	print("%.1f" % ((ix*2 + iix*3 + iiix*5) / 10))
	cn = cn + 1
