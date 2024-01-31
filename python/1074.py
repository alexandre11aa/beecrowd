### Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre umam
### ensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do
### valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá im
### primir apenas NULL. A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Ca
### da caso de teste a seguir é um valor inteiro X (-107 < X <107). Para cada caso, imprima uma mensagem correspondente, de acordo
### com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas nam
### esma linha. Q:1074

gg = int(input())

for i in range(gg):
	nu = int(input())
	if (nu > 0) and (nu % 2 == 0):
		print("EVEN POSITIVE")
	elif (nu > 0):
		print("ODD POSITIVE")
	elif (nu < 0) and (nu % 2 == 0):
		print("EVEN NEGATIVE")
	elif (nu < 0):
		print("ODD NEGATIVE")
	else:
		print("NULL")
