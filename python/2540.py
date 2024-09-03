#### Analógimôn Go! é um jogo bastante popular. Os jogadores de Analógimôn Go! são divididos em três grandes times: Time Valor, Tim
#### e Instinto e Time Místico, que são liderados pelos seus líderes Kandera, Esparky e Blanque, respectivamente. Naturalmente, voc
#### ê faz parte de um desses times! O líder do seu time está sendo acusado de infringir as regras do jogo por gerenciar incorretam
#### ente os doces recebidos do Professor que são destinados ao time. Isto criou uma grande polêmica dentro da equipe: alguns jogad
#### ores defendem que o líder realmente agiu incorretamente e deve sofrer um impeachment e ser afastado de seu cargo, enquanto out
#### ros defendem que ele não infringiu as regras, que a acusação é inverídica e que ele deve continuar no cargo. Para resolver a s
#### ituação, uma votação será realizada entre todos os N jogadores do seu time. Cada jogador deverá votar se o impeachment deve ou
#### não ocorrer. Se o número de votos favoráveis ao impeachment foi maior ou igual a 2/3 (dois terços) do total de jogadores, o lí
#### der será afastado. Caso contrário, a acusação é arquivada e ele continuará no cargo. Dados os votos de todos os jogadores, det
#### ermine o resultado da votação. A entrada contém vários casos de teste. A primeira linha de cada caso contém o inteiro N (1 ≤ N
#### ≤ 105), o número de jogadores em seu time. A próxima linha contém N inteiros v1, ..., vN (vi = 0 ou 1), indicando os votos dos
#### jogadores. O valor 1 indica um voto favorável ao impeachment, enquanto o valor 0 indica um voto contrário ao mesmo. A entradat
#### ermina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma linha contendo a palavra impeachment se o líder deve ser
#### afastado de seu cargo, ou acusacao arquivada caso contrário. Q:2540

while True:
	try:
		n = int(input())
		v = list(map(int,input().split()))

		s = 0

		for i in range(n):
			s += v[i]

		if s >= n * (2/3):
			print("impeachment")
		else:
			print("acusacao arquivada")

	except:
		break
