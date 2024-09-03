#### Chegamos finalmente no final do semestre e pra variar, trabalhos estão acumulados! Os professores, com a intenção de ajudar (
#### ou não), decidiram que os trabalhos será feitos em duplas, além disso, eles dariam o spoiler do grau de dificuldade que um tr
#### abalho tem para ser feito. Sabendo disso, Rangel, nosso velho amigo, escolheu Gugu como sua dupla, pois ele sabe que Gugu é u
#### m cara responsável. Como ambos estão apertados eles decidiram dividir os trabalhos com os seguintes critérios: A ordem dos tr
#### abalhos não pode ser alterada durante a divisão; A divisão precisa ser justa, ou seja, minimizar a diferença entre os trabalh
#### os feitos por Rangel e por Gugu; Rangel sempre faz os primeiros e trabalhos e Gugu o restante. Como os dois estão muito ocupa
#### dos na biblioteca pegando os livros para resolverem os trabalhos, eles pediram a você para determinar a diferença.  Entrada /
#### O arquivo contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 106) que indica o número d
#### e elementos da sequência, na segunda linha contém N inteiros onde cada inteiro possui um valor X (1 ≤ X ≤105). A entrada term
#### ina com um EOF. Saída / Para cada caso de teste, um inteiro Y deve ser impresso, onde Y é o valor da diferença ótima seguindo
#### os critérios do problema. Deixe uma linha em branco após cada caso de teste, inclusive após o último. Q:2715

while True:
    try:
        n = int(input())

        t = list(map(int,input().split()))

        if len(t) < n:
            while len(t) < n:
                t.append(int(input()))

        c, r, g = [0,0,0]

        tt, r_test = [sum(t), t[c]]

        while True:
            g_test = tt - r_test

            if r_test == g_test:
                print(0)
                break
            
            elif r_test > g_test:
                if (r_test - g_test) > (g - r):
                    print(g - r)
                else:
                    print(r_test - g_test)
                    
                break

            c += 1
            r = r_test
            g = g_test
            r_test += t[c]

    except:
        break
