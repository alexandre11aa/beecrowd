#### O seu professor de programação gostaria que você fizesse um programa com as seguintes características: Crie vinte e seis vari
#### áveis inteira; Atribua a primeira variável o valor 97; Atribua as outras demais variável o valor da primeira somado de uma un
#### idade; Mostre na tela os valores numéricos da primeira variável, um espaço em braco, o carácter 'e', outro espaço em branco e
#### o seu valor alfanumérico (caracteres); Repita o procedimento para todas as outras variáveis. Entrada / Não há. / Saída / O re
#### sultado de seu programa deve ser o mesmo do exemplo de saída. Q:2753

letras = ''' a b c d 
             e f g h 
             i j k l 
             m n o p 
             q r s t 
             u v w x 
             y z '''
             
lista = list(letras.split())

for i in range(len(lista)):
    print(str(97 + i) + ' e ' + lista[i])
