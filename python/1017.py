### Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz1
### 2 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecero
### tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, e
### m seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto. O arquivo de entrada c
### ontém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h)
### . Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal. Q:1017

t1 = float(input())
ve = float(input())

di = (t1 * ve)/12

print("%.3f" % di)
