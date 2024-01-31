#### Dodô, Leo e Pepper passam várias madrugadas conversando, em algum lugar do Condomínio Jardim Botânico IV. Diversos assuntos as
#### trais ganham pauta nestas conversas homéricas. Nas últimas sessões, Dodô tem falado do jogo de RPG que ele e Leo estão inventa
#### ndo, Leo (para “variar”, mas com razão) tem falado do gênero musical heavy metal e Pepper ficou fascinado com a história da mi
#### tologia grega contada por Leo. Os garotos resolveram adotar uma estratégia para dividir as sessões igualmente entre os assunto
#### s, de modo que eles possam especular cada um ao máximo e chegarem a conclusões astronômicas. Eles irão jogar “pedra, papel e t
#### esoura” para decidir o assunto da sessão de hoje, e então irão alternar os assuntos nas próximas sessões. Dadas as jogadas deD
#### odô, Leo e Pepper, nesta ordem, você deve determinar o assunto da sessão de hoje. A entrada é composta por vários casos de tes
#### te e termina com fim de arquivo. Cada caso de teste é composto por uma única linha, que contém as jogadas de cada um dos garot
#### os, como mostrado nos exemplos. Para cada caso de teste, imprima uma única linha com a mensagem "Os atributos dos monstros vao
#### ser inteligencia, sabedoria..." para indicar que Dodô é o vencedor, a mensagem "Iron Maiden's gonna get you, no matter how far
#### !" para indicar que Leo é o vencedor, a mensagem "Urano perdeu algo muito precioso..." para indicar que Pepper é o vencedor, o
#### u a mensagem "Putz vei, o Leo ta demorando muito pra jogar..." se houver empate. Q:2626

while True:
	try:
		j = list(input().split())

		d, l, p, x = [0,0,0,""]

		for i in range(3):
			if i == 0:
				a1, a2 = [1,2]
			elif i == 1:
				a1, a2 = [0,2]
			elif i == 2:
				a1, a2 = [0,1]

			for k in range(2):
				if k == 0:
					a0 = a1
				elif k == 1:
					a0 = a2

				if j[i] == "pedra":
					if j[a0] == "pedra":
						if i == 0:
							d += 1
						elif i == 1:
							l += 1
						elif i == 2:
							p += 1
					elif j[a0] == "tesoura":
						if i == 0:
							d += 2
						elif i == 1:
							l += 2
						elif i == 2:
							p += 2
				elif j[i] == "papel":
					if j[a0] == "papel":
						if i == 0:
							d += 1
						elif i == 1:
							l += 1
						elif i == 2:
							p += 1
					elif j[a0] == "pedra":
						if i == 0:
							d += 2
						elif i == 1:
							l += 2
						elif i == 2:
							p += 2
				elif j[i] == "tesoura":
					if j[a0] == "tesoura":
						if i == 0:
							d += 1
						elif i == 1:
							l += 1
						elif i == 2:
							p += 1
					elif j[a0] == "papel":
						if i == 0:
							d += 2
						elif i == 1:
							l += 2
						elif i == 2:
							p += 2

		if d == p and d == l and p == l:
			print("Putz vei, o Leo ta demorando muito pra jogar...")
		elif d != p and d != l and p != l:
			print("Putz vei, o Leo ta demorando muito pra jogar...")
		elif d == p or d == l or p == l:
			if d > p and d > l:
				print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
			elif l > d and l > p:
				print("Iron Maiden's gonna get you, no matter how far!")
			elif p > l and p > d:
				print("Urano perdeu algo muito precioso...")
			else:
				print("Putz vei, o Leo ta demorando muito pra jogar...")
		elif d > p:
			if d < l:
				print("Iron Maiden's gonna get you, no matter how far!")
			else:
				print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
		elif p > d:
			if p < l:
				print("Iron Maiden's gonna get you, no matter how far!")
			else:
				print("Urano perdeu algo muito precioso...")

	except:
		break
