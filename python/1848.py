#### Como se sabe, existe um corvo com três olhos. O que não se sabia é que o corvo com três olhos pode prever o resultado da lote
#### ria de Westeros. Enquanto todos os outros corvos coletam as apostas, o corvo de três olhos já sabe o resultado, e quando Bran
#### sonha com o corvo, o corvo conta o resultado. O problema é que Bran apesar de lembrar do sonho, não consegue interpretá-lo so
#### zinho em tempo hábil. A sua tarefa é fazer um programa para interpretar o sonho de Bran e calcular o resultado da loteria. Du
#### rante o sonho, o corvo pisca diversas vezes e grita apenas 3 vezes. A cada grito um número do resultado da loteria é calculad
#### o. Cada piscada do corvo comunica um número em binário. Um olho aberto significa 1 e um olho fechado significa 0. O olho da e
#### squerda é o mais significativo e o da direita é o menos significativo. A cada piscada, este número deve ser somado, e quandoo
#### corv o grita, essa soma é um resultado. A entrada descreve, em cada linha, em sequência, ou um grito ou uma piscada do corvo.
#### Um grito é representado pela string caw caw. Uma piscada é representada por três caracteres * ou -, representando, respectiva
#### mente, um olho aberto ou um olho fechado, da esquerda para a direita. Lembre-se que o corvo tem 3 olhos. Os números sorteados
#### na loteria não excedem 1000. A saída são três linhas, cada linha com um número da loteria. Q:1848

for i in range(3):
	con = 0

	while True:
		p = input()

		if p == "caw caw":
			print(con)
			break
		elif p == "--*":
			con += 1
		elif p == "-*-":
			con += 2
		elif p == "*--":
			con += 4
		elif p == "*-*":
			con += 5
		elif p == "**-":
			con += 6
		elif p == "-**":
			con += 3
		elif p == "***":
			con += 7
