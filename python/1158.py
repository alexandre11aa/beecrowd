### Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros Xe
### Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo: pa
### ra a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13 para a entrada 7 4, a saída deve ser 40, que é
### equivalente à: 7 + 9 + 11 + 13. A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a segu
### ir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y. Imprima a soma dos consecutivos números ímpares a p
### artir do valor X. Q:1158

con = int(input())

for i in range(con):
	x, y = map(int,input().split())
	
	soma = 0
	impares = x
	
	for j in range(1,y*2+1):
		if impares % 2 != 0:
			soma += impares
			
		impares += 1
		
	print(soma)
