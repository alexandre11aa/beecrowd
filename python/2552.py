
#196 Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha(
#### BH)! Nesta cidade, o jogo PãodeQueijoSweeper é bastante popular! O tabuleiro do jogo consiste em uma matriz de N linhas e M co
#### lunas. Cada célula da matriz contém um pão de queijo ou o número de pães de queijo que existem nas celulas adjacentes a ela. U
#### ma célula é adjacente a outra se estiver imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não cont
#### iver um pão de queijo, uma célula deve obrigatoriamente conter um número entre 0 e 4, inclusive. Dadas as posições dos pães de
#### queijo, determine o tabuleiro do jogo! A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiro
#### s N e M (1 ≤ N, M ≤ 100). As próximas N linhas contém M inteiros cada, separados por espaços, descrevendo os pães de queijo no
#### tabuleiro. O j-ésimo inteiro da i-ésima linha é 1 se existe um pão de queijo na linha i e coluna j do tabuleiro, ou 0 caso con
#### trário. A entrada termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima N linhas com M inteiros cada, não separad
#### os por espaços, descrevendo a configuração do tabuleiro. Se uma posição contém um pão de queijo, imprima 9 para ela; caso cont
#### rário, imprima o número cuja posição deve conter. Q:2552

while True:
	try:
		li, co = map(int,input().split())

		m, mf = [[],[]]

		for l in range(li):
			m.append(list(map(int,input().split())))

		for l in range(li):
			mf.append([])
			for c in range(co):
				mf[l].append(0)

		for l in range(li):
			for c in range(co):
				if m[l][c] == 1:
					mf[l][c] = 9
	
				else:
					if li == 1 and co == 1:
						if m[l][c] == 1:
							mf[l][c] = 9
						else:
							mf[l][c] = 0

					elif li == 1 and co > 1:
						if c == 0:
							mf[l][c] = m[l][c + 1]
						elif c == (co - 1):
							mf[l][c] = m[l][c - 1]
						else:
							mf[l][c] = m[l][c + 1] + m[l][c - 1]

					elif li > 1 and co == 1:
						if l == 0:
							mf[l][c] = m[l + 1][c]
						elif l == (li - 1):
							mf[l][c] = m[l - 1][c]
						else:
							mf[l][c] = m[l + 1][c] + m[l - 1][c]

					else:
						if l == 0 and c == 0:
							mf[l][c] = m[l + 1][c] + m[l][c + 1]
						elif l == 0 and c == (co - 1):
							mf[l][c] = m[l + 1][c] + m[l][c - 1]
	
						elif l == (li - 1) and c == 0:
							mf[l][c] = m[l - 1][c] + m[l][c + 1]
						elif l == (li - 1) and c == (co - 1):
							mf[l][c] = m[l - 1][c] + m[l][c - 1]

						elif l < (li - 1) and c == 0:
							mf[l][c] = m[l + 1][c] + m[l - 1][c] + m[l][c + 1]
						elif l < (li - 1) and c == (co - 1):
							mf[l][c] = m[l + 1][c] + m[l - 1][c] + m[l][c - 1]

						elif l == 0 and c < (co - 1):
							mf[l][c] = m[l + 1][c] + m[l][c + 1] + m[l][c - 1]
						elif l == (li - 1) and c < (co - 1):
							mf[l][c] = m[l - 1][c] + m[l][c + 1] + m[l][c - 1]

						else:
							mf[l][c] = m[l + 1][c] + m[l - 1][c] + m[l][c + 1] + m[l][c - 1]

		for l in range(li):
			p = ""
			for c in range(co):
				p += str(mf[l][c])

			print(p)
		
	except:
		break
