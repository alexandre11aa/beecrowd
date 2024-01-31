### A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo: |0 - 400.00 : 15% |4
### 00.01 - 800.00 : 12%|800.01 - 1200.00 : 10%|1200.01 - 2000.00 : 7%|Acima de 2000.00 : 4%|. Leia o salário do funcionárioe calc
### ule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual. A entrada contéma penasu
### m valor de ponto flutuante, com duas casas decimais. Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e op
### ercentual de reajuste ganho, conforme exemplo abaixo. Q:1048

sa = float(input())

if sa >= 0 and sa <= 400:
	resa = sa * 0.15
	nosa = sa + resa
	print("Novo salario: %.2f" % nosa)
	print("Reajuste ganho: %.2f" % resa)
	print("Em percentual: 15 %")

elif sa > 400 and sa <= 800:
	resa = sa * 0.12
	nosa = sa + resa
	print("Novo salario: %.2f" % nosa)
	print("Reajuste ganho: %.2f" % resa)
	print("Em percentual: 12 %")

elif sa > 800 and sa <= 1200:
	resa = sa * 0.1
	nosa = sa + resa
	print("Novo salario: %.2f" % nosa)
	print("Reajuste ganho: %.2f" % resa)
	print("Em percentual: 10 %")

elif sa >= 1200 and sa <= 2000:
	resa = sa * 0.07
	nosa = sa + resa
	print("Novo salario: %.2f" % nosa)
	print("Reajuste ganho: %.2f" % resa)
	print("Em percentual: 7 %")

elif sa > 2000:
	resa = sa * 0.04
	nosa = sa + resa
	print("Novo salario: %.2f" % nosa)
	print("Reajuste ganho: %.2f" % resa)
	print("Em percentual: 4 %")

else:
	print("Valor impossível de se calcular.")
