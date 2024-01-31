#### A cifra mais antiga conhecida é a Cifra de César. César escrevia suas cartas trocando cada letra pela próxima do alfabeto, par
#### a evitar que, quando a carta fosse interceptada, conseguissem ler. Com o tempo, a criptografia adquiriu melhor qualidade, masa
#### criptografia por substituição ainda é uma brincadeira de criança interessante, por exemplo: ZEN I T | POLAR . Neste tipo de br
#### incadeira, ao escrever uma carta a letra Z é trocada pela letra P e vice versa, bem como: E e O e assim sucessivamente. A fras
#### e cifrada desta forma: "Osro roxre osri caftide" pode ser decifrada como: "Este texto esta cifrado". Como a brincadeira ficous
#### éria, a você foi solicitado um programa que decifre as mensagens cifradas a partir de uma chave fornecida. A entrada contém vá
#### rios casos de teste. Cada caso de teste começa com uma linha indicando dois números inteiros C e N, 0 < C < 21 e 0 < N < 100.C
#### é o tamanho da cifra. Nas duas linhas seguintes está a cifra de tamanho C indicando quais caracteres da primeira linha será su
#### bstituído por caracteres da segunda linha, um caracter aparece uma única vez, na primeira ou na segunda linha. A cifra pode co
#### nter letras de ‘A’ a ‘Z’, números de ‘0’ a ‘9’ além do espaço em branco e alguns símbolos de pontuação: '.' ',' ';' ':' '(' ')
#### ' '!' e '?'. Nas próximas N linhas estão frases e sentenças criptografadas pela cifra fornecida, que você deve decifrar. Cadal
#### inha contém no mínimo 1 e no máximo 1000 caracteres. São permitidos quaisquer caracteres ASCII (não extendido) imprimíveis, ne
#### ste caso não estão presentes nenhum caracter acentuado, nem mesmo 'ç'. Para cada caso de teste da entrada seu programa deve ge
#### rar para cada linha de frase e sentença de entrada, uma linha com a saída decifrada, respeitando a capitalização da letra (let
#### ras maiúsculas são decifradas como maiúsculas e minúsculas como minúsculas quando for possível aplicar a diferenciação, se não
#### for possível serão decifrados como letras minúsculas). Após cada caso de teste deve ser impressa uma linha em branco, inclusiv
#### e após o último. Q:2502

while True:
	try:
		c, n = map(int,input().split())

		let = input()
		cif = input()

		for i1 in range(n):
			frase = input()
			
			tradl = []
			tradp = ""

			for i2 in range(len(frase)):
				tradl.append(frase[i2])

			for i3 in range(c):
				for i4 in range(len(frase)):
					if frase[i4].lower() == cif[i3].lower():
						if tradl[i4].isupper() == True:
							tradl[i4] = let[i3].upper()
						else:
							tradl[i4] = let[i3].lower()
					elif frase[i4].lower() == let[i3].lower():
						if tradl[i4].isupper() == True:
							tradl[i4] = cif[i3].upper()
						else:
							tradl[i4] = cif[i3].lower()

			for i5 in range(len(frase)):
				tradp += tradl[i5]

			print(tradp)

		print("")

	except:
		break
