### Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada p
### onto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (n
### esta situação sem escrever mensagem alguma). A entrada contém vários casos de teste. Cada caso de teste contém 2 valores intei
### ros. Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida. Q:1115

con = True

while con == True:
	x, y = map(int,input().split())
	if x == 0 or y == 0:
		con = False
	else:
		if x > 0 and y > 0:
			print("primeiro")
		elif x < 0 and y > 0:
			print("segundo")
		elif x < 0 and y < 0:
			print("terceiro")
		else:
			print("quarto")
