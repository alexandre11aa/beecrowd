#### Assim como a maioria dos estudantes de computação, você vive jogando os jogos eletrônicos mais populares atualmente: Liga of L
#### egendas (LOL) e Contra-Strike (CS). Embora você também jogue LOL, você gosta mais é de usar todas suas grandes habilidades par
#### a derrotar a equipe terrorista em Contra-Strike! Você é tão empenhado no combate ao terror que é frequentemente comparado como
#### presidente dos EUA que anunciou a captura e derrota de um grande terrorista da vida real. Por ser bastante habilidoso, os víde
#### os de suas jogadas (seus famosos gameplays) vivem aparecendo na Jogatina UFPR, uma página na internet que publica gameplays de
#### alunos da universidade. A página publica muitos vídeos diariamente. Por isso, pode ser dificil encontrar e contar todos os seu
#### s vídeos na página. Entretanto, como você também é programador, você decidiu escrever um programa para auxiliá-lo nesta tarefa
#### . Dada a lista de gameplays publicados na página, determine quantos gameplays seus de Contra-Strike foram publicados. A entrad
#### a contém vários casos de teste. A primeira linha de cada caso contém dois inteiros N e I (1 ≤ N ≤ 104, 1000 ≤ I ≤ 9999), o núm
#### ero de gameplays publicados na página e o seu identificador na universidade, respectivamente. As próximas N linhas descrevem o
#### s gameplays publicados. Cada gameplay é descrito por dois inteiros i e j (1000 ≤ i ≤ 9999, j=0 ou 1), onde i é o identificador
#### na universidade do autor do gameplay, e j=0 se o gameplay é de Contra-Strike, ou j=1 se é de Liga of Legendas. A entrada termi
#### na com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma única linha com um número indicando quantos gameplays seus d
#### e Contra-Strike foram publicados na página. Q:2543

while True:
	try:
		qntd, cred = map(int,input().split())

		s = 0

		for i in range(qntd):
			crdd, cs = map(int,input().split())

			if crdd == cred and cs == 0:
				s += 1

		print(s)

	except:
		break
