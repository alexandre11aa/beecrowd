### Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se est
### es valores foram digitados em ordem crescente ou decrescente. A entrada contém vários casos de teste. Cada caso contém dois va
### lores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y. Para cada caso de teste imprima
### “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”. Q:1113

con = True

while con == True:
	n, m = map(int,input().split())
	if n == m:
		con = False
	else:
		if n < m:
			print("Crescente")
		else:
			print("Decrescente")
