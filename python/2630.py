#### Alguns algoritmos de processamento de imagem exigem um pré-processamento no qual é necessário transformar uma imagem colorida
#### em uma imagem em tons de cinza. Esta conversão pode ser realizada de diversas maneiras, dependendo do resultado que se preten
#### de obter. Para preservar a percepção das cores básicas pelo olho humano, uma conversão apropriada seria tomar 30% da componen
#### te vermelha (R), 59% da componente verde (G) e 11% da componente azul (B). Em termos matemáticos, P = 0, 30R + 0, 59G + 0, 11
#### B | Outras abordagens possíveis seriam determinar o valor de P através da média aritmética das três componentes ou atribuir a
#### P os valores da maior ou da menor entre as três componentes. Dadas as componentes RGB de um pixel da imagem colorida, determi
#### ne o valor do pixel P da imagem em tons de cinza correspondente, determinada a conversão a ser utilizada. Despreze a parte de
#### cimal do resultado, caso exista. A entrada em T (1 ≤ T ≤ 100) casos de teste, onde o valor de T é dado na primeira linha da e
#### ntrada. Cada caso de teste é composto por duas linhas: a primeira linha contém a conversão a ser utilizada: eye para a primei
#### ra abordagem descrita, mean para a média aritmética, max para o valor da maior componente e min para o valor da menor compone
#### nte. A segunda linha contém os valores R, G, B (0 ≤ R, G, B ≤ 255) do pixel da imagem colorida. Para cada caso de testes deve
#### r ser impressa a seguinte mensagem "Caso #t: P", onde P é o nível de cinza do pixel da imagem em tons de cinza após a convers
#### ão do pixel da imagem colorida. Esta mensagem deve ser seguida de uma quebra de linha. Q:2630

T = int(input())

for j in range(T):
    conversao = input()
    valores = list(map(int,input().split()))

    if conversao == "eye":
        print("Caso #%i: %i" % (j + 1, int(0.30 * valores[0] + 0.59 * valores[1] + 0.11 * valores[2])))
    elif conversao == "mean":
        print("Caso #%i: %i" % (j + 1, int((valores[0] + valores[1] + valores[2]) / 3)))
    elif conversao == "max":
        print("Caso #%i: %i" % (j + 1, int(max(valores))))
    elif conversao == "min":
        print("Caso #%i: %i" % (j + 1, int(min(valores))))
