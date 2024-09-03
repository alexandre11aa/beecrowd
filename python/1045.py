### Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lad
### os. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma m
### ensagem adequada: se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO ; se A2 = B2 + C2, apresente a mensagem: TRIANGULO RET
### ANGULO ; se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO ; se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTA
### NGULO ; se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO ; se apenas dois dos lados forem iguais, apr
### esente a mensagem: TRIANGULO ISOSCELES ; A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 <
### B) e C (0 < C). Imprima todas as classificações do triângulo especificado na entrada. Q:1045

la, lb, lc = input().split()

la = float(la)
lb = float(lb)
lc = float(lc)

if lc > lb:
	xx = lb
	lb = lc
	lc = xx

if lb > la:
	xx = la
	la = lb
	lb = xx

if lc > lb:
	xx = lb
	lb = lc
	lc = xx

if la >= lb + lc:
	print("NAO FORMA TRIANGULO")

elif (la**2 == lb**2 + lc**2):
	print("TRIANGULO RETANGULO")
	if (la == lb or la == lc or lb == lc):
		print("TRIANGULO ISOSCELES")

elif (la**2 > lb**2 + lc**2):
	print("TRIANGULO OBTUSANGULO")
	if (la == lb == lc):
		print("TRIANGULO EQUILATERO")
	elif (la == lb or la == lc or lb == lc):
		print("TRIANGULO ISOSCELES")

elif (la**2 < lb**2 + lc**2):
	print("TRIANGULO ACUTANGULO")
	if (la == lb == lc):
		print("TRIANGULO EQUILATERO")
	elif (la == lb or la == lc or lb == lc):
		print("TRIANGULO ISOSCELES")
