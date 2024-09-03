#### Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma l
#### ista de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5. Esse desafio pode parecer simples,p
#### orém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um progra
#### ma para resolver o desafio de Bino. A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quanti
#### dade de números na lista de Bino. A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bi
#### no. Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos, p
#### ois ela deve ser seguida rigorosamente. Q:2060

con = int(input())
l = list(map(int,input().split()))

m2 = 0
m3 = 0
m4 = 0
m5 = 0

for i in range(con):
	if l[i] % 2 == 0:
		m2 += 1
	if l[i] % 3 == 0:
		m3 += 1
	if l[i] % 4 == 0:
		m4 += 1
	if l[i] % 5 == 0:
		m5 += 1

print("%.i Multiplo(s) de 2" % m2)
print("%.i Multiplo(s) de 3" % m3)
print("%.i Multiplo(s) de 4" % m4)
print("%.i Multiplo(s) de 5" % m5)
