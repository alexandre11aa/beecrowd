#### O seu professor gostaria de fazer um programa com as seguintes características: Crie duas variáveis para armazenar números re
#### ais de precisão simples; Crie duas variáveis para armazenar números reais de precisão dupla; Leia o primeiro número de precis
#### ão simples que sempre terá uma casa decimal; Leia o segundo número de precisão simples que sempre terá duas casas decimais; L
#### eia o primeiro número de precisão dupla que sempre terá três casas decimais; Leia o segundo número de precisão dupla que semp
#### re terá quatro casas decimais; Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armaze
#### nado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual
#### , um espaço em branco, o número armazenado na segunda variável lida no passo 4. Não esqueça de pular linha; Imprima a letra C
#### , um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável lida no passo 5, uma v
#### irgula, um espaço em branco, a letra D, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na se
#### gunda variável lida no passo 6. Não esqueça de pular linha; Repita o procedimento 7, imprimindo os números com uma casa decim
#### al; Repita o procedimento 8, imprimindo os números com uma casa decimal; Repita o procedimento 7, imprimindo os números com d
#### uas casas decimais; Repita o procedimento 8, imprimindo os números com duas casas decimais; Repita o procedimento 7, imprimin
#### do os números com três casas decimais; Repita o procedimento 8, imprimindo os números com três casas decimais; Repita o proce
#### dimento 7, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E; Repita o procedim
#### ento 8, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E; Repita o procediment
#### o 7, imprimindo somente a parte inteira do número; Repita o procedimento 8, imprimindo somente a parte inteira do número. / E
#### ntrada / A entrada consiste em vários arquivos de teste. Em cada arquivo de teste tem duas linhas. Na primeira linha tem dois
#### números reais A e B (-1000.0 ≤ A, B ≤ 1000.0), separados por espaço em branco. Na segunda linha tem dois números reais C e  D
#### (-1000.0 ≤ C, D ≤ 1000.0), separados por espaço em branco. Conforme mostrado no exemplo de entrada a seguir. / Saída / Para c
#### ada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem doze linhas da forma descrita no item 7 e 8. Conform
#### e mostra o exemplo de saída a seguir. Q:2758

import struct

def truncar(num, n):
    n_X = struct.pack('<f', num)
    X = struct.unpack('<f', n_X)

    X_t = str(round(X[0], n))

    itr = len(str(int(X[0])))

    while True:
        if len(X_t[itr:]) <= n:
            X_t += "0"
            
        else:
            break

    return str(X_t)

A, B = map(float,input().split())
C, D = map(float,input().split())

print('A = %s, B = %s\nC = %.6f, D = %.6f' % (truncar(A, 6), truncar(B, 6), C, D))
print('A = %s, B = %s\nC = %.1f, D = %.1f' % (truncar(A, 1), truncar(B, 1), C, D))
print('A = %s, B = %s\nC = %.2f, D = %.2f' % (truncar(A, 2), truncar(B, 2), C, D))
print('A = %s, B = %s\nC = %.3f, D = %.3f' % (truncar(A, 3), truncar(B, 3), C, D))
print('A = %.3E, B = %.3E\nC = %.3E, D = %.3E' % (A, B, C, D))
print('A = %.0f, B = %.0f\nC = %.0f, D = %.0f' % (A, B, C, D))
