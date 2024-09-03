## Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calculao
## salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais. O arquivo de entrada c
## ontém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor q
## ue o funcionário recebe por hora trabalhada, respectivamente. Imprima o número e o salário do funcionário, conforme exemplo forn
## ecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.Q
## :1008

num = int(input())
hr = float(input())
shr = float(input())

slr = hr * shr

print("NUMBER =",num)
print("SALARY = U$ %.2f" % slr)
