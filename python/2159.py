#### Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos atén
#### , para n ≥ 17. Esta quantidade é representada pela função (n). Sua tarefa é, dado um natural n, calcular o mínimo e máximo doi
#### ntervalo para o número aproximado de primos até n. A entrada é um número natural n (17 ≤ n ≤ 109). A saída são dois valores Pe
#### M com 1 casa decimal cada, tal que P < (n) < M, de acordo com a fórmula dada acima. Os valores devem ser separados por um espa
#### ço em branco. Q:2159

import math

n = int(input())

print("%.1f %.1f" % (n/math.log(n), 1.25506 * (n/math.log(n))))
