### Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorre ta informada
### , escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permiti
### do" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. A entrada é composta por vários casos de testes con
### tendo valores inteiros. Para cada valor lido mostre a mensagem correspondent e à descrição do problema. Q:1114

con = True

while con == True:
	senha = int(input())
	if senha == 2002:
		print("Acesso Permitido")
		con = False
	else:
		print("Senha Invalida")
