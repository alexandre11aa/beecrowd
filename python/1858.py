#### Ramsay: "(...) você vence se conseguir adivinhar quem eu sou e por que estou torturando você." Theon deve pensar rápido e adi
#### vinhar quem é seu algoz! Entretanto, Ramsay já decidiu o que ele irá fazer depois que Theon der sua resposta. Theon pode dize
#### r que seu algoz é alguma dentre N pessoas. Considere que as pessoas são numeradas de 1 a N. Se Theon responder que seu algozé
#### a pessoa i, Ramsay irá atingi-lo Ti vezes. Sua tarefa é ajudar Theon a determinar qual deve ser sua resposta de forma a minim
#### izar o número de vezes que ele será atingido. A primeira linha contém um inteiro N (1 ≤ N ≤ 100). A segunda linha contém N in
#### teiros T1, T2, ..., TN (0 ≤ Ti ≤ 20). Imprima uma linha contendo o número da pessoa que Theon deve dizer ser seu algoz. Se ex
#### iste mais de uma resposta possível, imprima a menor. Q:1858

qtd = int(input())
nmrs = list(map(int,input().split()))

con = 1
nmr = nmrs[0]

for i in range(qtd):
	if nmrs[i] < nmr:
		nmr = nmrs[i]
		con = i + 1
	
print(con)
