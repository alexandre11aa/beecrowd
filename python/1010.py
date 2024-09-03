### Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça2
### , o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago. O arquivo de entrada contém
### duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais. A saída de
### verá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o
### "R$". O valor deverá ser apresentado com 2 casas após o ponto. Q:1010

p1, v1, vu1 = input().split()
p2, v2, vu2 = input().split()

v1 = float(v1)
vu1 = float(vu1)
v2 = float(v2)
vu2 = float(vu2)

va1 = v1 * vu1
va2 = v2 * vu2
vat = va1 + va2

print("VALOR A PAGAR: R$ %.2f" % vat)
