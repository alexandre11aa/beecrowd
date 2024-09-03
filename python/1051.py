### Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não exi
### stem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda dest
### e país é o Rombus, cujo símbolo é o R$. Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb.
### Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo. Lembre que, se o
### salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$2
### 000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que
### resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais. A entrada contém apenas um valor de ponto flu
### tuante, com duas casas decimais. Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com du
### as casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento". Q:1051

imposto = float(input())

if (imposto >= 0 and imposto <= 2000):
	print("Isento")

elif (imposto > 2000 and imposto <= 3000):
	nimposto = imposto - 2000
	pnimposto = nimposto * 0.08
	print("R$ %.2f" % pnimposto)

elif (imposto > 3000 and imposto <= 4500):
	nimposto = imposto - 3000
	pnimposto = nimposto * 0.18
	pnimp = pnimposto + 80
	print("R$ %.2f" % pnimp)

else:
	nimposto = imposto - 4500
	pnimposto = nimposto * 0.28
	pnimp = pnimposto + 350
	print("R$ %.2f" % pnimp)
