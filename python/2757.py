#### O seu professor gostaria que você fizesse um programa com as seguintes características: Crie três variáveis para armazenar nú
#### meros inteiros; Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000; Leia o segundo número, que pod
#### e ser um valor na faixa de: 0 ≤ B ≤ 99; Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999; Imprima a let
#### ra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável, uma virgula, um e
#### spaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variáv
#### el, uma virgula, um espaço em branco, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazen
#### ado na terceira variável. Não esqueça de pular linha; Repita o procedimento 5, colocando o número em um espaçamento de 10 díg
#### itos e justificado a direita; Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e preenchido com ze
#### ros; Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a esquerda. Entrada / A entrad
#### a consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem um inteiro A (-10000 ≤ A
#### ≤ 10000). Na segunda linha tem um inteiro B (0 ≤ B ≤ 99). Na terceira linha tem um inteiro C (0 ≤ C ≤ 999). Conforme mostrado
#### no exemplo de entrada a seguir. / Saída / Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quat
#### ro linhas da forma descrita no item 5. Conforme mostra o exemplo de saída a seguir. Q:2757

nmr_1 = int(input())
nmr_2 = int(input())
nmr_3 = int(input())

lista_n = [str(nmr_1), str(nmr_2), str(nmr_3)]

print('A = %s, B = %s, C = %s' % (lista_n[0], lista_n[1], lista_n[2]))

for i in range(3):
    zero = ''
    espc = ''

    n = len(lista_n[i])

    for j in range(10 - n):
        zero += '0'
        espc += ' '

    if i == 0:
        p_1 = 'A = %s, ' % (espc + lista_n[i])

        if lista_n[i][0] == '-':
            p_2 = 'A = %s, ' % ('-' + zero + lista_n[i][1:n])

        else:
            p_2 = 'A = %s, ' % (zero + lista_n[i])

        p_3 = 'A = %s, ' % (lista_n[i] + espc)

    elif i == 1:
        p_1 += 'B = %s, ' % (espc + lista_n[i])
        p_2 += 'B = %s, ' % (zero + lista_n[i])
        p_3 += 'B = %s, ' % (lista_n[i] + espc)

    else:
        p_1 += 'C = %s' % (espc + lista_n[i])
        p_2 += 'C = %s' % (zero + lista_n[i])
        p_3 += 'C = %s' % (lista_n[i] + espc)

print(p_1+'\n'+p_2+'\n'+p_3)
