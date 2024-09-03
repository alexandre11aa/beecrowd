#### Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa carto
#### lina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas
#### de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo. Nes
#### te problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possí
#### vel selecionar três varetas, dentre as quatro, e formar um triângulo. A entrada é composta por apenas uma linha contendo quat
#### ro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100). Seu programa deve produzir apenas uma linha contendo apenas um caract
#### ere, que deve ser ‘S’ caso seja possível formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo. Q:1929

a, b, c, d = map(int,input().split())

if a + b > c and b + c > a and a + c > b:
	print("S")
elif a + b > d and b + d > a and a + d > b:
	print("S")
elif b + c > d and c + d > b and b + d > c:
	print("S")
elif a + c > d and c + d > a and a + d > c:
	print("S")
else:
	print("N")
