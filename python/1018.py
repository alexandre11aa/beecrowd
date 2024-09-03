### Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As no
### tas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias. O arquivo dee
### ntrada contém um valor inteiro N (0 < N < 1000000). Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada ti
### po necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu progra
### ma apresentará a mensagem: “Presentation Error”. Q:1018

val = int(input())

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

print(val)
print("%.i nota(s) de R$ 100,00" % va100)
print("%.i nota(s) de R$ 50,00" % va50)
print("%.i nota(s) de R$ 20,00" % va20)
print("%.i nota(s) de R$ 10,00" % va10)
print("%.i nota(s) de R$ 5,00" % va5)
print("%.i nota(s) de R$ 2,00" % va2)
print("%.i nota(s) de R$ 1,00" % va1)
