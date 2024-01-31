#### A popularização das redes WiFi aumentou a taxa de perda de informações sendo transferidas, uma vez que diversos fatores do mei
#### o ambiente podem facilmente comprometer os dados durante o tráfego. A URI, Unidade de Recuperação de Informações, tem como pri
#### ncipal objetivo identificar e corrigir erros em mensagens enviadas via redes WiFi. A técnica utilizada pela URI para identific
#### ação de erros é o teste de paridade, o qual pode ser descrito da seguinte forma: Seja S uma mensagem que será enviada de um di
#### spositivo para outro. Antes de S ser enviada, um bit extra B é adicionado no final da representação binária de S. Se a mensage
#### m S tiver um número par de bits de valor 1, o bit extra B terá valor 0. Caso contrário, se S tiver um número ímpar de bits dev
#### alor 1, B terá valor 1. Desta forma, após a inserção do bit B, a mensagem S terá um número par de bits de valor 1. Quando o de
#### stinatário recebe a mensagem S ele faz a contagem de bits de valor 1. Se a quantidade for par, significa que a mensagem chegou
#### com sucesso. Caso contrário, significa que a mensagem sofreu uma alteração e não está correta. Sua tarefa é escrever um algori
#### tmo que faça a inserção do bit B na mensagem S, de forma que após a inserção a mensagem S tenha um número par de bits de valor
#### 1. Cada caso de teste consiste em uma linha contendo a mensagem S, a qual consiste em no mínimo 1 e no máximo 100 bits. Imprim
#### a uma linha contendo a mensagem S adicionada do bit extra B. Q:2176

nmr = input()

pxi = 0
for i in range(len(nmr)):
	 pxi += int(nmr[i])

if pxi % 2 == 0:
	nmr += "0"
else:
	nmr += "1"

print(nmr)
