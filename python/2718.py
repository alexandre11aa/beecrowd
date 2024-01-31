#### Giovanna adora o Natal. As festas, a família, decorações natalinas e principalmente os famosos pisca pisca led. Porém, esse a
#### no a pequena Gio ficou triste ao perceber que seu jogo de luzes está quebrado. Algumas luzes ainda funcionam, outras não. Gio
#### vanna quer, obviamente, consertar seu objeto preferido mas não tem lâmpadas o suficiente pra substituir todas as queimadas en
#### tão resolveu fazer o seguinte: dividir o pisca pisca em grupos ordenados de 50 lâmpadas e em cada grupo só consertar a  maior
#### quantidade de lâmpadas consecutivas queimadas. Por serem muitos grupos, a tarefa se tornou tediosa e para tentar remediar iss
#### o, Giovanna, observando a semelhança dos grupos com representação binária de números quando imaginava lâmpadas queimadas como
#### 1's e lâmpadas funcionais como 0's, decidiu pensar neles efetivamente como números e escreveu as representações decimais dess
#### es binários então tentou descobrir a quantidade de lâmpadas a serem trocadas a partir dessas anotações. Sua tarefa é, dado as
#### anotações de Gio, diga quantas lâmpadas serão trocadas em cada grupo. Entrada / A primeira linha da entrada contém um  número
#### inteiro N (1 ≤ N ≤ 10**3) representando a quantidade de grupos que Giovanna anotou. As próximas N linhas contém um inteiro  X
#### ca da uma representando o equivalente decimal do número que representa o grupo. Saída / A saída consiste de N linhas cada uma
#### contendo o tamanho da maior sequência de lâmpadas consecutivas queimadas em cada grupo, respeitando a ordem de entrada dos gr
#### upos. Q:2718

n = int(input())

for i in range(n):
    decimal = int(input())
    
    binario = []
    
    while True:
        binario.append(decimal % 2)
        decimal = int(decimal / 2)
        
        if decimal <= 1:
            binario.append(decimal)
            binario.reverse()
            break
        
    contador, sequencia = [0,[]]
    
    for j in range(len(binario)):
        if binario[j] == 1:
            contador += 1
            
        elif binario[j] == 0:
            sequencia.append(contador)
            contador = 0

    sequencia.append(contador)

    sequencia.sort(reverse = True)
    
    print(sequencia[0])
