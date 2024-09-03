#### Imagine que você tenha uma máquina do tempo que pode ser usada no máximo três vezes, e a cada uso da máquina você pode escolhe
#### r voltar para o passado ou ir para o futuro. A máquina possui três créditos fixos; cada crédito representa uma certa quantidad
#### e de anos, e pode ser usado para ir essa quantidade de anos para o passado ou para o futuro. Você pode fazer uma, duas ou três
#### viagens, e cada um desses três créditos pode ser usado uma vez apenas. Por exemplo, se os créditos forem 5, 12 e 9, você poder
#### ia decidir fazer duas viagens: ir 5 anos para o futuro e, depois, voltar 9 anos para o passado. Dessa forma, você terminaria q
#### uatro anos no passado, em 2012. Também poderia fazer três viagens, todas indo para o futuro, usando os créditos em qualquer or
#### dem, terminando em 2042. Neste problema, dados os valores dos três créditos da máquina, seu programa deve dizer se é ou não po
#### ssível viajar no tempo e voltar para o presente, fazendo pelo menos uma viagem e, no máximo, três viagens; sempre usando cadau
#### m dos três créditos no máximo uma vez. A entrada consiste de uma linha contendo os valores dos três créditos A, B e C (1 ≤ A,B
#### , C ≤ 1000). Seu programa deve imprimir uma linha contendo o caracter “S” se é poss ível viajar e voltar para o presente, ou “
#### N” caso contrário. Q:2235

p1, p2, p3 = map(int,input().split())

if p1 == p2 or p1 == p3 or p2 == p3:
	print("S")
elif p1 + p2 == p3 or p1 + p3 == p2 or p2 + p3 == p1:
	print("S")
else:
	print("N")
