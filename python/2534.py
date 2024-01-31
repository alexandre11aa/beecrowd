#### Todo ano bissexto é realizado o exame geral de matemática da Nlogônia. Todos os cidadões da nação são avaliados a fim de se es
#### tudar o desenvolvimento lógico e matemático do país ao longo dos anos. Após as correções, os cidadões são ordenadados de acord
#### o com suas notas (quanto maior, melhor) e recebem descontos no imposto de renda de acordo com sua qualificação. O Escritório C
#### entral de Estatística (ECE) é encarregado de processar os dados das notas obtidas no exame. Entretanto este ano, Vasya, um dos
#### responsáveis, está internado no hospital com gripe H1N1 e você foi contratado para realizar o seu trabalho. Escreva um program
#### a que dado o número de habitantes da Nlogônia e todas as notas obtidas, responda as consultas para retornar a nota do cidadãoq
#### ue ficou em determinada posição. A entrada contém vários casos de teste. A primeira linha de cada caso contém dois inteiros N(
#### 1 ≤ N ≤ 100), Q (1 ≤ Q ≤ 100), o número de habitantes do país e o número de consultas, respectivamente. As N linhas seguintesc
#### ontém, cada uma, a nota ni obtida pelo i-ésimo cidadão (0 ≤ ni ≤ 30000). As próximas Q linhas contém cada uma uma consulta, ap
#### osição pi (1 ≤ pi ≤ N) a qual a ECE está interessada em saber a nota. A entrada termina com fim-de-arquivo (EOF). Para cada ca
#### so de teste, imprima, para cada consulta, uma linha contendo a nota do cidadão que ficou classificado na posição pi. Q:2534

while True:
	try:
		n, p = map(int,input().split())

		nmr, nmi, psç = [[],[],[]]

		for i in range(n):
			nmr.append(int(input()))
	
		nmr.sort()

		for i in range(n):
			nmi.append(nmr[n - 1 - i])
			
		for i in range(p):
			psç.append(int(input()))

		for i in range(p):
			print(nmi[psç[i] - 1])

	except:
		break
