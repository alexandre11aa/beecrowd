### A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depo
### is dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeir
### os números dessa série. O arquivo de entrada contém um valor inteiro N (0 < N < 46). Os valores devem ser mostrados na mesma l
### inha, separados por um espaço em branco. Não deve haver espaço após o último valor. Q:1151

nmr = int(input())

fib = 1
num = 0
let = "0 1"

while nmr > 2:
	fib += num
	num = fib - num
	let += " " + str(fib)
	nmr -= 1

print(let)
