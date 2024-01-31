### Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes
### , mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo. Leia três va
### lores de ponto flutuante (double) A, B e C. Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossive
### l calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente confor
### me exemplo abaixo. Imprima sempre o final de linha após cada mensagem. Q:1036

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B**2) - (4*A*C)

if (delta >= 0 and A != 0):
    x1 = (-B + delta**(1/2))/(2*A)
    x2 = (-B - delta**(1/2))/(2*A)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
else:
    print("Impossivel calcular")
