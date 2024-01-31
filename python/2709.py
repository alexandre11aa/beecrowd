#### Robbie é um robô muito carismático, e uma das coisas que ele mais gosta de fazer, além de brincar com Glória, é colecionar mo
#### edas. Robbie possui várias moedas com valores iguais ou diferente, e de mesmo mesmo tamanho. e elas são guardadas de maneirao
#### rganizada uma sobre a outra dentro de um cilindro de vidro. Robbie sempre faz um joguinho com Glória usando suas moedas quand
#### o ela pede pra brincar com ele de esconde-esconde, ou quando ela pede pra ele levá-la para passear. O jogo acontece da seguin
#### te maneira: Glória escolhe um número N que será o salto das moedas que serão somadas, então a cada Nmoedas o valor Vi da moed
#### a é somado até que não haja mais moedas, ou seja, Σ de ((VM-(N*0))+(VM-(N*1))+(VM-(N*2) )...), M é o número de moedas. Por ex
#### emplo, se existirem 5 moedas com os valores 1, 2 , 3, 4 e 5, e Glória escolher 2 como valor do salto, então serão somadas asm
#### oedas 5, 3 e 1, resultando em 9, ao final Robbie verifica se a soma dessas moedas é um número primo, se isso acontecer ele fa
#### z o que a Glória quer, caso contrário, a garotinha convence Robbie a jogar novamente, pois ela sempre consegue convencer eled
#### e tudo, alegando que deixará de contar histórias pra ele, caso ele não faça a vontade dela. Você como um bom programador da U
#### .S. Robots, ajudará esses dois amigos, escrevendo um programa irá dizer o resultado do jogo. A entrada contém vários casos de
#### teste. A primeira linha de um caso de teste contém um inteiro M (2 ≤ M ≤ 20 ) que representa a quantidade de moedas. Cada uma
#### das próximas M linhas contém um inteiro Vi (1 ≤ Vi ≤ 500) que representa o valor da moeda Mi , e por último um inteiro N (1 ≤
#### N ≤ M) que é o salto na soma escolhido por Glória. A entrada termina em EOF. Imprima “You’re a coastal aircraft, Robbie, a la
#### rge silver aircraft.”, caso Glória ganhe o jogo, ou “Bad boy! I’ll hit you.”, caso Glória não ganhe o jogo. A saída não devec
#### onter aspas. Q:2709

while True:
    try:
        quantidade = int(input())

        numeros, numero, primo = [[],0,0]

        for i in range(quantidade):
            numeros.append(int(input()))

        posicao = len(numeros) - 1

        salto = int(input())

        while True:
            numero += numeros[posicao]
        
            posicao -= salto

            if posicao < 0:
                break

        divi = numero - 1

        if divi == 0:
            print("Bad boy! I’ll hit you.")

        lgc = True

        while lgc == True and divi >= 1:
            if (numero % divi == 0) and (divi != 1):
                print("Bad boy! I’ll hit you.")
                lgc = False
            elif divi == 1:
                print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
            divi = divi - 1

    except:
        break
