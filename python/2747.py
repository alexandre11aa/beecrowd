#### O seu professor de programação gostaria de fazer uma tela com as seguintes características: Ter 39 traços (-) na primeira lin
#### ha; Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em  branco;
#### Repita o procedimento 2 mais quatro vezes; Repita o procedimento 1. No final deve ficar igual a imagem a seguir: ------------
#### --------------------------- (39 traços) / |                                     | / |                                     | /
#### |                                     | / |                                     | / |                                     | /
#### --------------------------------------- (39 traços) / Entrada / Não há. / Saída / A saída será impresso conforme a figura aci
#### ma. Q:2747

tracos = '---------------------------------------'
barras = '|                                     |'

for i in range(7):
    if (i == 0) or (i == 6):
        print(tracos)

    else:
        print(barras)
