#### Há muito tempo atrás, em uma galáxia muito, muito distante... Após o declínio do Império, sucateiros estão espalhados por todo
#### o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cer
#### cado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para umt
#### erreno 4 x 7 com um sabre de luz nele (na posição (2, 4)). Você deve escrever um programa que, dado um terreno N x M, procurap
#### elo padrão do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de luz. A primeira linha da entrada temd
#### ois números positivos N e M, representando, respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ N, M ≤ 1
#### 000). Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos em cada célula do terreno (-100 ≤ Tij ≤ 10
#### 0, para 1 ≤ i ≤ N e 1 ≤ j ≤ M). A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles representam a coo
#### rdenada (X,Y) do sabre de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero. Q:2163

li, co = map(int,input().split())

m = []
s = "0 0"

for i in range(li):
	m.append(list(map(int,input().split())))

for l in range(li):
	for c in range(co):
		if m[l][c] == 42:
			if (li-1 > l > 0) and (co-1 > c > 0):
				if m[l-1][c+1] == 7 and m[l][c+1] == 7 and m[l+1][c+1] == 7:
					if m[l-1][c] == 7 and m[l+1][c] == 7:
						if m[l-1][c-1] == 7 and m[l][c-1] == 7 and m[l+1][c-1] == 7:
							s = str(l + 1) + " " + str(c + 1)

print(s)
