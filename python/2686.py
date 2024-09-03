#### Novamente Júlio pede sua ajuda, ele esqueceu de um pequeno detalhe. Como o seu o programa anterior só informava uma saudação,
#### ele pediu que transformasse o grau do Sol/Lua em HH:MM:SS. Então caso aceite: dado um grau relativo a posição do Sol/Lua, ref
#### aça o sistema só que agora além da saudação de cada período do dia, informe exatamente as horas, os minutos e segundos. A ent
#### rada contem um pontos flutuantes M (0 ≥ M < 360) representando a posição, em graus,do Sol/Lua em relação a terra. Como eles a
#### ndam em constante movimento seu programa receberá diversos casos a cada segundo(EOF). Imprima qual período do dia ele se enco
#### ntra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De Madrugada!!", e na linhas de baixo exiba as horas, minutos e segundos (
#### HH:MM:SS). Q:2686

def org(x):
    if (x - int(x)) > 0.98:
        x = round(x)
    else:
        x = int(x)

    if len(str(x)) == 1:
        x = "0" + str(x)
    else:
        x = str(x)

    return x

while True:
    try:
        horario = float(input())

        if   0 <= horario < 90 or horario == 360:
            print("Bom Dia!!")
        elif 90 <= horario < 180:
            print("Boa Tarde!!")
        elif 180 <= horario < 270:
            print("Boa Noite!!")
        elif 0 <= horario < 360:
            print("De Madrugada!!")

        hrs = 6 + (horario / 15)

        if hrs >= 24:
            hrs -= 24

        mns = ((horario / 15) - int(horario / 15)) * 60

        if (mns - int(mns)) > 0.98:
            mns = round(mns)

        sgs = (mns - int(mns)) * 60

        print("%s:%s:%s" % (org(hrs), org(mns), org(sgs)))

    except:
        break
