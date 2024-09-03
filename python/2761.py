#### O seu professor gostaria de fazer um programa com as seguintes características: Crie uma variável inteira; Crie uma  variável
#### real de simples precisão; Crie uma variável que armazene um carácter; Crie uma variável que armazene uma frase de no máximo 5
#### 0 caracteres; Leia todas as variáveis na ordem da forma criada; Imprima todas as variáveis como foram lidas; Imprima as variá
#### veis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas; Imprima as variáveis com exatos 10 espaços. Entra
#### da A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem uma variável A que armaze
#### na um número inteiro, uma variável B que armazena um número real, uma variável C com um carácter e uma variável D que armazen
#### a uma frase de no máximo 50 caracteres. Conforme mostrado no exemplo de entrada a seguir. Saída Para cada arquivo da entrada,
#### terá um arquivo de saída. O arquivo de saída tem três linhas da forma descrita nos itens 6, 7 e 8. Conforme mostra o  exemplo
#### de saída a seguir. Imprima os valores de ponto flutuante com 6 casas decimais após a vírgula. Q:2761

import struct

v_1, v_2, v_3, v_4 = input().split(" ", maxsplit = 3)

v_1 = int(v_1)
v_2 = float(v_2)

n_X = struct.pack('<f', v_2)
X = struct.unpack('<f', n_X)

v_2 = X[0]

print('%d%.6f%c%s'         % (v_1, v_2, v_3, v_4))
print('%d\t%.6f\t%c\t%s'   % (v_1, v_2, v_3, v_4))
print('%10d%10.6f%10c%10s' % (v_1, v_2, v_3, v_4))
