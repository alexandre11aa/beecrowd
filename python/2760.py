#### O seu professor gostaria de fazer um programa com as seguintes características: Crie 3 variáveis para armazenar uma frase  de
#### no máximo 100 caracteres; Leia uma frase para a primeira variável; Leia uma frase para a segunda variável; Leia uma frase par
#### a a terceira variável; Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável l
#### ida no passo 4. Não esqueça de pular linha; Imprima a primeira variável lida no passo 3, a segunda variável lida no passo  4,
#### a terceira variável lida no passo 2. Não esqueça de pular linha; Imprima a primeira variável lida no passo 4, a segunda variá
#### vel lida no passo 2, a terceira variável lida no passo 3. Não esqueça de pular linha; Repita o procedimento 5, imprimindo  só
#### 10 caracteres de cada variável. / Entrada / A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três li
#### nhas. Na primeira linha tem uma variável A que armazena uma frase de no máximo 100 caracteres. Na segunda linha tem uma variá
#### vel B que armazena uma frase de no máximo 100 caracteres. Na terceira linha tem uma variável C que armazena uma frase de no m
#### áximo 100 caracteres. Conforme mostrado no exemplo de entrada a seguir. Saída Para cada arquivo da entrada, terá um arquivo d
#### e saída. O arquivo de saída tem quatro linhas da forma descrita nos itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a s
#### eguir.Q:2760

def dez(frase):
    if len(frase) > 10:
        frase = frase[:10]

    return frase

frase_1 = input()
frase_2 = input()
frase_3 = input()

print(frase_1 + frase_2 + frase_3)
print(frase_2 + frase_3 + frase_1)
print(frase_3 + frase_1 + frase_2)

print(dez(frase_1) + dez(frase_2) + dez(frase_3))
