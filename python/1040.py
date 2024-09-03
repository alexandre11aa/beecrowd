### Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calculea
### média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media:
### ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, impr
### ima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimi
### r a mensagem "Aluno em exame.". No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo alun
### o. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com
### a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais )
### ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego ex
### ame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno. A entrada contém quatro nú
### meros de ponto flutuante correspendentes as notas dos alunos. Todas as respostas devem ser apresentadas com uma casa decimal.A
### s mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha,c
### aso contrário obterá "Presentation Error". Q:1040

pn, sn, tn, qn = input().split()

pn = float(pn)
sn = float(sn)
tn = float(tn)
qn = float(qn)

pm = (pn*2 + sn*3 + tn*4 + qn*1)/10

if pm >= 7:
	print("Media: %.1f" % pm)
	print("Aluno aprovado.")
elif pm < 5:	
	print("Media: %.1f" % pm)
	print("Aluno reprovado.")
else:
	print("Media: %.1f" % pm)
	print("Aluno em exame.")
	exame = float(input())
	print("Nota do exame: %.1f" % exame)
	sm = (exame + pm)/2
	if sm >= 5:
		print("Aluno aprovado.")
		print("Media final: %.1f" % sm)
	else:
		print("Aluno reprovado.")
		print("Media final: %.1f" % sm)
