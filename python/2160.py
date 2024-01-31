#### Preencher formulários é uma tarefa simples. Mas é preciso conferir se o espaço reservado para os dados é suficiente. Sua taref
#### a é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres. A entrada é uma linha de tex
#### to L (1 ≤ |L| ≤ 500). A saída é dada em uma única linha. Ela deve ser "YES" (sem as aspas) se a linha de texto L tem até 80 ca
#### racteres. Se L tem mais de 80 caracteres, a saída deve ser "NO". Q:2160

nome = input()

if len(nome) > 80:
	print("NO")
else:
	print("YES")
