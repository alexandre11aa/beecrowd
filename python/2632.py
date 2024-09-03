#### No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As magias são elem
#### entais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do nível da magia. A tabela
#### abaixo lista cada magia, o dano e o respectivo raio por nível: Magia: Fire - Dano: 200 - Lvl1: 20 - Lvl 2: 30 - Lvl 3: 50 ; M
#### agia: Water - Dano: 300 - Lvl1: 10 - Lvl 2: 25 - Lvl 3: 40 ; Magia: Earth - Dano: 400 - Lvl1: 25 - Lvl 2: 55 - Lvl 3: 70 ; Ma
#### gia: Air - Dano: 100 - Lvl1: 18 - Lvl 2: 38 - Lvl 3: 60 ; As unidades inimigas são delimitadas por um retângulo de largura we
#### altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador te
#### nha qualquer intercessão com a área deﬁnida pelo círculo da magia. Dada a posição e o retângulo delimitador da unidade inimig
#### a, o centro da explosão e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a unidade esteja for
#### a do alcance da magia, o dano sofrido é igual a zero. A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor deT
#### é informado na primeira linha da entrada. Cada caso de teste é composto por duas linhas. A primeira contém quatro número inte
#### iros que repre-sentam as dimensões w e h (1 ≤ w, h ≤ 1000) do retângulo e as coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto
#### inferior esquerdo. A segunda linha do caso de teste contém uma string com o identiﬁcador da magia (ﬁre para fogo, water paraá
#### gua, earth para terra e air para ar), o nível N desta magia (1 ≤ N ≤ 3) e as coordenadas cx e cy (0 ≤ cx, cy ≤ 1000) do centr
#### o da área da explosão. Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido de uma quebra
#### de linha. Q:2632

T = int(input())

def distancia(x_r, y_r, x_c, y_c, raio):
    dist = (((x_r-x_c)**2) + ((y_r-y_c)**2))**(1/2)

    if  dist > raio:
        print(0)
    else:
        print(circulo[0])

for j in range(T):
    validador = "pode printar"
    
    retangulo = list(map(int,input().split()))
    circulo = list(input().split())

    if   circulo[0] == "fire":
        circulo[0] = "200"
        if   circulo[1] == "1":
            circulo[1] = "20"
        elif circulo[1] == "2":
            circulo[1] = "30"
        elif circulo[1] == "3":
            circulo[1] = "50"

    elif circulo[0] == "water":
        circulo[0] = "300"
        if   circulo[1] == "1":
            circulo[1] = "10"
        elif circulo[1] == "2":
            circulo[1] = "25"
        elif circulo[1] == "3":
            circulo[1] = "40"

    elif circulo[0] == "earth":
        circulo[0] = 400
        if   circulo[1] == "1":
            circulo[1] = "25"
        elif circulo[1] == "2":
            circulo[1] = "55"
        elif circulo[1] == "3":
            circulo[1] = "70"

    elif circulo[0] == "air":
        circulo[0] = 100
        if   circulo[1] == "1":
            circulo[1] = "18"
        elif circulo[1] == "2":
            circulo[1] = "38"
        elif circulo[1] == "3":
            circulo[1] = "60"

    coord_ret_xy = [(retangulo[2], retangulo[3]), #ponto inferior esquerdo
                    (retangulo[2] + retangulo[0], retangulo[3]), #ponto inferior direito
                    (retangulo[2], retangulo[3] + retangulo[1]), #ponto superior esquerdo
                    (retangulo[2] + retangulo[0], retangulo[3] + retangulo[1])] #ponto superior direito

    # entre-polos dos círculos

    if   int(circulo[2]) < coord_ret_xy[0][0]:
        if   int(circulo[3]) < coord_ret_xy[0][1]:
            validador = "já printou"
            distancia(coord_ret_xy[0][0], coord_ret_xy[0][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

        elif int(circulo[3]) > coord_ret_xy[2][1]:
            validador = "já printou"
            distancia(coord_ret_xy[0][0], coord_ret_xy[2][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

    elif int(circulo[2]) > coord_ret_xy[1][0]:
        if   int(circulo[3]) <= coord_ret_xy[1][1]:
            validador = "já printou"
            distancia(coord_ret_xy[1][0], coord_ret_xy[1][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

        elif int(circulo[3]) >= coord_ret_xy[3][1]:
            validador = "já printou"
            distancia(coord_ret_xy[1][0], coord_ret_xy[3][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

    # polos dos círculos

    if   int(circulo[2]) >= coord_ret_xy[0][0] and int(circulo[2]) <= coord_ret_xy[1][0] :
        if   int(circulo[3]) <= coord_ret_xy[0][1] and validador == "pode printar":
            distancia(int(circulo[2]), coord_ret_xy[0][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

        elif int(circulo[3]) >= coord_ret_xy[2][1] and validador == "pode printar":
            distancia(int(circulo[2]), coord_ret_xy[2][1], int(circulo[2]), int(circulo[3]), int(circulo[1]))

        else:
            print(circulo[0])

    elif int(circulo[3]) >= coord_ret_xy[0][1] and int(circulo[3]) <= coord_ret_xy[2][1]:
        if   int(circulo[2]) <= coord_ret_xy[0][0] and validador == "pode printar":
            distancia(coord_ret_xy[0][0], int(circulo[3]), int(circulo[2]), int(circulo[3]), int(circulo[1]))

        elif int(circulo[2]) >= coord_ret_xy[1][0] and validador == "pode printar":
            distancia(coord_ret_xy[1][0], int(circulo[3]), int(circulo[2]), int(circulo[3]), int(circulo[1]))

        else:
            print(circulo[0])
