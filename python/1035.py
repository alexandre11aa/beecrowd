### Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maio
### r que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senã
### o escrever "Valores nao aceitos". Quatro números inteiros A, B, C e D. Mostre a respectiva mensagem após a validação dos valor
### es. Q:1035

A, B, C, D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
	print("Valores aceitos")

else:
    print("Valores nao aceitos")
