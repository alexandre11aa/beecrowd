#### Juvenal comportou-se muito bem este ano, já que gosta muito de química e queria muito ganhar um kit Alquimia. Entretanto, Juv
#### enal pediu para incluir alguns elementos perigosos em seu kit. Seu Noel não podendo negar o pedido ( afinal, como dizer não p
#### ara a criança mais bem comportada do planeta?) pediu para o pobre elfo Patatatitu garantir que o presente fosse seguro. Patat
#### atitu sabe muito sobre química, e conhece todos os compostos perigosos que podem ser feitos com os elementos disponíveis no k
#### it de Juvenal. Assim, decidiu enviar um cd junto com o presente, contendo um programa que afira a segurança dos  experimentos
#### de Juvenal. Todos concordam que a criança mais bem-comportada do planeta nunca faria uma experiência sem antes checar sua seg
#### urança conforme as instruções. Porém Patatatitu não sabe programar e está atrás de ajuda. Você poderia ajudá-lo? Para facilit
#### ar, Patatatitu explica que um composto perigoso é formado a partir da mistura de elementos na ordem de sua fórmula atômica  e
#### respeitando as devidas proporções. Neste kit de química é possível apenas adicionar um elemento por vez, em diferentes quanti
#### dades. Assim para formar trifluoreto de cloro (ClF3), um composto muito perigoso, deve-se adicionar um átomo cloro (Cl) e trê
#### s de flúor (F3), independentemente do que for adicionado antes ou depois. ClF4 não é um composto perigoso, pois está fora  de
#### proporção. De forma similar caso Mg2F seja um composto perigoso, Mg2Fe será seguro, visto que flúor (F) é um elemento distint
#### o de ferro (Fe). Entrada / A entrada consiste de um inteiro N (0 < N < 10) que indica o número de casos de teste. Cada caso d
#### e teste consiste em um inteiro T (0 < T < 51) que indica o número de compostos perigosos possíveis, caso os elementos sejam i
#### ncluídos na ordem e proporções mostradas. Seguem T linhas, cada uma contendo uma string de até 50 caracteres representando um
#### a formula que gera um composto perigoso caso os elementos sejam misturados na ordem e proporções que são apresentados. Após i
#### sso, é dado um inteiro U (0 < U < 51) que indica a quantia de experiencias que Juvenal irá realizar. Seguem U linhas cada uma
#### contendo uma string de até 50 caracteres representando os elementos que Juvenal utilizara na ordem e proporções em que  serão
#### adicionados. Saída / A saída consiste de U linhas por caso de teste, as quais devem informar se Juvenal deve prosseguir ou ab
#### ortar o  U-ésimo  experimento do caso teste. Caso deva abortar imprima "Abortar", caso seja seguro imprima "Prossiga".  Deixe
#### uma linha em branco entre cada caso de teste. Q:2724

N = int(input())

for i in range(N):
    T = int(input())

    c, e = [[], []]
    
    for j in range(T):
        c.append(input())

    U = int(input())

    for j in range(U):
        e.append(input())
 
    for j in range(U):
        validacao = 0
        
        for k in range(T):
            posicao = e[j].find(c[k])

            m, n = [len(c[k]), posicao + len(c[k])]

            if posicao == 0:
                
                if m == len(e[j]):
                    validacao += 1
                    break

                elif ((e[j][n]).isdigit() !=  True) and ((e[j][n]).isupper() ==  True):
                    validacao += 1
                    break
                    
            elif posicao > 0:
                
                if n == len(e[j]):
                    validacao += 1
                    break

                elif ((e[j][n]).isdigit() !=  True) and ((e[j][n]).isupper() ==  True):
                    validacao += 1
                    break

        if validacao > 0:
            print('Abortar')

        else:
            print('Prossiga')

    if i < N - 1:
        print()
