#### Você fica tão feliz no natal que tem vontade de gritar para todo mundo: "Feliz natal!!". Pra colocar toda essa felicidade pra f
#### ora, você montou um programa que, colocado um índice I de felicidade, seu grito de natal é mais animado. A entrada é composta p
#### or um inteiro I (1 < I ≤ 104) que representa o índice de felicidade. A saída é composta pela frase "Feliz natal!", sendo repeti
#### das I vezes a última letra a da frase. Uma quebra de linha é necessária após a impressão da frase. Q:2483

a = int(input())

s = "Feliz nat"

for i in range(a):
	s += "a"

print(s + "l!")
