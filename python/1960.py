#### A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as página
#### s de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, quando nec
#### essário, dividem o livro em volumes. Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na num
#### eração romana. Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000. A entrada é um número i
#### nteiro positivo N (0 < N < 1000). A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiús
#### culas. Q:1960

nmr = input()

nmrF, e = [float(nmr), len(nmr)]
i, ii, iii = ["","",""]
casa = e

for i in range(e):
	con = nmr[i]

	if casa == 3:
		n3 = ["0","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
		if con != "0":
			iii = n3[int(con)]
		else:
			iii = ""

	elif casa == 2:
		n2 = ["0","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
		if con != "0":
			ii = n2[int(con)]
		else:
			ii = ""

	else:
		n1 = ["0","I","II","III","IV","V","VI","VII","VIII","IX"]
		if con != "0":
			i = n1[int(con)]
		else:
			i = ""

	casa -= 1

print(iii + ii + i)
