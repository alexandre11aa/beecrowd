#### Os cientistas da NASA descobriram um novo exoplaneta que fica a 1 bilhão de anos luz da terra. O nome desse planeta foi batiza
#### do de Pronalândia em homenagem aos novos cientistas que estão sendo formados no PRONATEC. Só que o mais incrível ainda está po
#### r vir. Ao observar melhor o planeta eles conseguiram identificar que os habitantes da Pronalândia estavam querendo se comunica
#### r por uma numeração. Só que a numeração que encontraram está invertida e como encontraram muitas delas chamaram você para cons
#### eguir automatizar esse processo. Logo, dado um número grande, sua tarefa é imprimir esse número invertido. O arquivo contém ap
#### enas uma linha de teste que é o número encontrado (0 < n < 9999999999). Obs.: Perceba que o número lido é muito alto para arma
#### zenar em uma variável do tipo int, logo você irá precisar utilizar o tipo long, que para a leitura e impressão em C, você deve
#### utilizar o %llu. Imprimir o número lido invertido. Não esqueça de imprimir a quebra de linha (\n) no final, caso contrário voc
#### ê receberá (Presentation Error). Q:1984

n = int(input())

print(str(n)[::-1])
