### Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor n
### úmero de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As m
### oedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias. O arquivo de entrada c
### ontém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00). Imprima a quantidade mínima de notas e moedas necessárias para trocar
### o valor inicial, conforme exemplo fornecido. Obs: Utilize ponto (.) para separar a parte decimal. Q:1021

val = float(input())

x = val

va100 = x / 100
x = x % 100

va50 = x / 50
x = x % 50

va20 = x / 20
x = x % 20

va10 = x / 10
x = x % 10

va5 = x / 5
x = x % 5

va2 = x / 2
x = x % 2

va1 = x
x = x % 1

va050 = x / 0.5
x = x % 0.5

va025 = x / 0.25
x = x % 0.25

va010 = x / 0.10
x = x % 0.10

va005 = x / 0.05
x = x % 0.05

va001 = x / 0.01
va001 = round(va001)

print("NOTAS:")
print("%.i nota(s) de R$ 100.00" % va100)
print("%.i nota(s) de R$ 50.00" % va50)
print("%.i nota(s) de R$ 20.00" % va20)
print("%.i nota(s) de R$ 10.00" % va10)
print("%.i nota(s) de R$ 5.00" % va5)
print("%.i nota(s) de R$ 2.00" % va2)
print("MOEDAS:")
print("%.i moeda(s) de R$ 1.00" % va1)
print("%.i moeda(s) de R$ 0.50" % va050)
print("%.i moeda(s) de R$ 0.25" % va025)
print("%.i moeda(s) de R$ 0.10" % va010)
print("%.i moeda(s) de R$ 0.05" % va005)
print("%.i moeda(s) de R$ 0.01" % va001)
