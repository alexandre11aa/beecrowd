#### Na geometria Euclidiana, um polígono regular é um polígono em que todos os ângulos são iguais e todos os lados tem o mesmo com
#### primento. Um polígono simples é aquele cujos segmentos de reta não se interceptam. Abaixo pode-se ver vários mosaicos feitos p
#### or polígonos regulares. Você deve escrever um programa que, dados o número e o comprimento dos lados de um polígono regular, m
#### ostre seu perímetro. A entrada tem dois inteiros positivos: N e L, que são, respectivamente, o número de lados e o comprimento
#### de cada lado de um polígono regular (3 ≤ N ≤ 1000000 and 1 ≤ L ≤ 4000). A saída é o perímetro P do polígono regular em uma úni
#### ca linha. Q:1959

n, l = map(int,input().split())

print(n * l)
