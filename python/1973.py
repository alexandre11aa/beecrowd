#### Após comprar vários sítios adjacentes na região do oeste catarinense, a família Estrela construiu uma única estrada que passap
#### or todos os sítios em sequência. O primeiro sítio da sequência foi batizado de Estrela 1, o segundo de Estrela 2, e assim pord
#### iante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e resolveu fazer uma Jornada nas Estrelas para roubar carneir
#### os das propriedades de seus irmãos. Mas ele está definitivamente pirado. Quando passa pelo sítio Estrela i, ele rouba apenas u
#### m carneiro daquele sítio (se o sítio tem algum) e segue ou para Estrela i + 1 ou para Estrela i - 1, dependendo se o número de
#### carneiros em Estrela i era, respectivamente, ímpar ou par. Se não existe a Estrela para a qual ele deseja seguir, ele interrom
#### pe sua jornada. O irmão louco começa sua Jornada em Estrela 1, roubando um carneiro do seu próprio sítio. A primeira linha dae
#### ntrada consiste de um único inteiro N (1 ≤ N ≤ 106), o qual representa o número de Estrelas. A segunda linha da entrada consis
#### te de N inteiros, de modo que o i-ésimo inteiro, Xi (1 ≤ Xi ≤ 106), representa o número inicial de carneiros em Estrela i. Imp
#### rima uma linha contendo dois inteiros, de modo que o primeiro represente o número de Estrelas atacadas pelo irmão louco e o se
#### gundo represente o número total de carneiros não roubados. Q:1973

n = int(input())
e = list(map(int,input().split()))

r, c, s, l, p = [0,0,0,[0],""]

for i in range(len(e)):
	s += e[i]

for i in range(len(e)):
	if i % 2 == 0 and i != l[0]:
		break

	if e[i] == 1:
		if l[0] == 0:
			l[0] = 1
		else:
			l.append(i + 1)

while True:
	if e[c] == 0:
		r += 1
		break

	if e[c] % 2 != 0:
		r += 1
		if r == len(e):
			break
	else:
		p = "v"
		r = (r * 2) + 1
		break

	c += 1

if p == "v":
	print(int(r/2 + 0.5),(s - r + l[len(l) - 1]))
else:
	print(r,s - r)
