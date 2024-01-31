#### Ao observar a curva de velocidade de um motor, o engenheiro Zé percebeu que sempre ocorria uma queda quando as medidas eram fe
#### itas em intervalos de 10 ms. Mas esta queda acontecia em medidas diferentes a cada novo teste do motor. Zé ficou curioso com e
#### ssa falta de padrão e quer saber, para cada teste do motor, qual a primeira medida em que ocorre uma queda de velocidade. A en
#### trada é um teste do motor e é dada em duas linhas. A primeira tem o número N de medidas de velocidade do motor (1 < N ≤ 100).A
#### segunda linha tem N inteiros: o número de RPM (rotações por minuto) Ri de cada medida (0 ≤ Ri ≤ 10000, para todo Ri, tal que 1
#### ≤ i ≤ N). Uma medida é considerada uma queda se é menor que a medida anterior. A saída é o índice da medida em que houve a pri
#### meira queda de velocidade no teste. Caso não aconteça uma queda de velocidade a saída deve ser o número zero. Q:2167

qntd = int(input())
nmrs = list(map(int,input().split()))

t = 0

for i in range(qntd):
	if i < qntd - 1:
		if nmrs[i] > nmrs[i + 1]:
			t = i + 2
			break

print(t)
