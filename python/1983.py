#### As aulas do Prof. Jatobá estão dando o que falar. Os representantes do MEC vieram até a UNIME de Lauro de Freitas para saber m
#### ais detalhes sobre essa nova forma de ensinar Algoritmos. Além disso, eles queriam selecionar 1 aluno para participar da OBI-T
#### ec (Olimpíada Brasileira de Informática Nível Técnica) e representar a rede Kroton na competição, pois sabem que lá estão os m
#### elhores. Para selecionar o melhor, eles têm disponível uma lista com o número de inscrição de cada aluno e a sua respectiva no
#### ta na disciplina. Sua tarefa é ajudar o pessoal do MEC a encontrar o aluno mais apto a representar a instituição e quem sabe g
#### arantir sua vaga. Só tem um detalhe, se a nota mais alta não for maior ou igual a 8, você deverá imprimir “Minimum note not re
#### ached”. O arquivo contém primeiro a quantidade de alunos (3 <= n <= 100) existentes e em seguida, os n alunos contendo o númer
#### o da matrícula (0 < m < 1000000) de cada um, seguido da respectiva nota (0 <= nota <= 10.0, com 1 casa decimal). Obs.: as nota
#### s não serão repetidas. Ou seja, não tem chance de ter dois alunos com a mesma nota. Você deve imprimir o número do estudante q
#### ue obteve a maior pontuação ou "Minimum note not reached" (sem aspas) caso nenhum estudante tenha tirado uma nota maior ou igu
#### al a 8. Q:1983

n = int(input())
nome = 0
nota = 0

for i in range(n):
	nom, no = input().split()
	if float(no) > float(nota):
		nome = nom
		nota = no

if float(nota) < 8:
	print("Minimum note not reached")
else:
	print(nome)
