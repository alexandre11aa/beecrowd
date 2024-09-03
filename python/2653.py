#### No jogo O Bruxo, Sigismund Dijkstra é o líder do Serviço Secreto Redaniano, por causa disso ele é uma das pessoas mais import
#### antes do mundo. Além disso Dijkstra possui um grande tesouro, o qual possui diversos tipos de jóias. Dijkstra está muito curi
#### oso para saber quantos tipos de jóias diferentes seu tesouro possui. Sabendo que você é o melhor programador do continente Di
#### jkstra te contratou para verificar quantos tipos de jóias distintas ele tem em seu tesouro. A entrada consiste de várias linh
#### as e cada uma contém uma string que descreve uma das jóias de Dijkstra. Essa string é composta apenas dos caracteres '(' e ')
#### ', a soma do tamanho de todas as string não excede 106. Imprima quantos tipos de jóias distintas Dijkstra tem. Q:2653

list_joias = []

try:
    while True:
        joia = input()

        '''
        if len(set(list(joia))) == 1:
            if (list(set(list(joia))))[0] != "(" and (list(set(list(joia))))[0] != ")":
                break

        else:
            if (list(set(list(joia))))[0] != "(" and (list(set(list(joia))))[0] != ")":
                break

            if (list(set(list(joia))))[0] != "(" and (list(set(list(joia))))[0] != ")":
                break
        '''

        if joia not in list_joias:
            list_joias.append(joia)

except:
    print(len(list_joias))
