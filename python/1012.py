### Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre: a) a á
### rea do triângulo retângulo que tem A por base e C por altura. b) a área do círculo de raio C. (pi = 3.14159) c) a área do trapé
### zio que tem A e B por bases e C por altura. d) a área do quadrado que tem lado B. e) a área do retângulo que tem lados A e B. O
### arquivo de entrada contém três valores com um dígito após o ponto decimal. O arquivo de saída deverá conter 5 linhas de dados.C
### ada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e ov
### alor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal. Q:1012

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

tri = (A * C)/2
cir = 3.14159 * (C**2)
tra = ((A + B)*C)/2
qua = B**2
ret = A * B

print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % qua)
print("RETANGULO: %.3f" % ret)
