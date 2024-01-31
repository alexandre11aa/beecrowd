#### Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite para saber se estão consumindo a quantidade recomendadad
#### iária de vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para escrever um programa que, dado o consumo diáriod
#### e alimentos ricos em vitamina C por uma pessoa, indique o quanto essa pessoa deve consumir a mais ou a menos para atingir o rec
#### omendado. Para tal, você poderá utilizar a tabela a seguir: Alimentos ricos em Vitamina C	| Quantidade de Vitamina C - (suco d
#### (e laranja	120 mg) - (morango fresco 85 mg) - (mamao 85 mg) - (goiaba vermelha 70 mg) - (manga 56 mg) - (laranja 50 mg) - (broc
#### (olis 34 mg). Considere que o consumo diário recomendado de vitamina C está entre 110 mg e 130 mg, inclusive. Cada caso de test
#### e é composto um inteiro T (1 ≤ T ≤ 7) indicando que a pessoa consome diariamente T alimentos entre os 7 alimentos da tabela. Em
#### seguida, haverá T linhas com um inteiro N e um alimento (totalmente em caixa baixa e sem acentuações), indicando que a pessoa c
#### onsome uma quantidade N daquele alimento. A entrada termina com T = 0. Para cada caso de teste (T), se o consumo ultrapassou ol
#### imite recomendado, imprima "Menos X mg", em que X representa a quantidade a menos a ser consumida para atingir o limite recomen
#### dado; se o consumo não atingiu o recomendado, imprima "Mais X mg", em que X representa a quantidade a mais para atingir o recom
#### endado; se o consumo está dentro do intervalo recomendado, imprima "X mg", em que X representa a quantidade consumida diariamen
#### te pela pessoa. Q:2486

ali = ["suco", "morango", "mamao", "goiaba", "manga", "laranja", "brocolis"]
vtc = [120, 85, 85, 70, 56, 50, 34]

while True:
	qntd = int(input())

	if qntd == 0:
		break

	s = 0

	for i in range(qntd):
		c = 0

		l = list(input().split())
		
		for j in range(7):
			if ali[j] == l[1]:
				c = vtc[j] * int(l[0])
				break

		s += c

	if s < 110:
		print("Mais", (110 - s), "mg")
	elif s > 130:
		print("Menos", (s - 130), "mg")
	else: 
		print(s, "mg")
