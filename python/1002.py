## A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: - Efe
## tue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. A entrada contém um valor de ponto flutuante(
## dupla precisão), no caso, a variável raio. Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abai
## xo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de impr
## imir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error". Q:1002

ra = float(input())

acc = (ra**2)*3.14159

print("A=%.4f" % acc)
