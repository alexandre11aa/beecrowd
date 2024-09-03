#### A fórmula de Binet é uma forma de calcular números de Fibonacci. Sua tarefa é, dado um natural n, calcular o valor de Fibonacc
#### i(n) usando a fórmula. A entrada é um número natural n (0 < n ≤ 50). A saída é o valor de Fibonacci(n) com 1 casa decimal util
#### izando a fórmula de Binet dada. Q:2164

n = float(input())

fi = (((1 + 5**(1/2))/2)**(n) - ((1 - 5**(1/2))/2)**(n))/(5**(1/2))

print("%.1f" % fi)
