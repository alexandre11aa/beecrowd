#### Júlio está criando um novo Smart Watch especialmente para programadores. É impressionante as vantagens que ele oferece e o co
#### nforto pra codar que ele tem. O relógio ainda está em desenvolvimento e ele prometeu consertar os bugs e colocar uns apetrech
#### os melhores e, em troca, pediu um sistema simples para o modo Standy Bay. O problema é que o relógio por si só sempre tem o â
#### ngulo de inclinação do Sol/Lua(de 0 a 360). Valendo um relógio, caso deseja aceitar: dada em grau da inclinação do Sol/Lua, i
#### nforme em qual período do dia ele se encontra. A entrada contém um número inteiro M (0 ≤ M ≤ 360) representando o grau do Sol
#### /Lua. Como a posição muda constantemente seu programa receberá diversos casos a cada segundo(EOF). Imprima uma saudação refer
#### ente ao período do dia que ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De Madrugada!!". Q:2685

while True:
    try:
        horario = int(input())

        if   0 <= horario < 90 or horario == 360:
            print("Bom Dia!!")
        elif 90 <= horario < 180:
            print("Boa Tarde!!")
        elif 180 <= horario < 270:
            print("Boa Noite!!")
        elif 0 <= horario < 360:
            print("De Madrugada!!")

    except:
        break
