#### Rosy é uma talentosa professora do Ensino Médio que já ganhou muitos prêmios pela qualidade de sua aula. Seu reconhecimento foi
#### tamanho que foi convidada a dar aulas em uma escola da Inglaterra. Mesmo falando bem inglês, Rosy ficou um pouco apreensiva com
#### a responsabilidade, mas resolveu aceitar a proposta e encará-la como um bom desafio. Tudo ocorreu bem para Rosy até o dia da pr
#### ova. Acostumada a dar notas de 0 (zero) a 100 (cem), ela fez o mesmo na primeira prova dos alunos da Inglaterra. No entanto, os
#### alunos acharam estranho, pois na Inglaterra o sistema de notas é diferente: as notas devem ser dadas como conceitos de A a E. O
#### conceito A é o mais alto, enquanto o conceito E é o mais baixo. Conversando com outros professores, ela recebeu a sugestão de u
#### tilizar a seguinte tabela, relacionando as notas numéricas com as notas de conceitos: O problema é que Rosy já deu as notas nos
#### istema numérico, e terá que converter as notas para o sistema de letras. Porém, Rosy precisa preparar as próximas aulas (para m
#### anter a qualidade que a tornou reconhecida), e não tem tempo suficiente para fazer a conversão das notas manualmente. Você deve
#### escrever um programa que recebe uma nota no sistema numérico e determina o conceito correspondente. A entrada contém um único c
#### onjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A entrada contém uma única linha
#### com um número inteiro N (0 ≤ N ≤ 100), representando uma nota de prova no sistema numérico. Seu programa deve imprimir, na saíd
#### a padrão, uma letra (A, B, C, D, ou E em maiúsculas) representando o conceito correspondente à nota dada na entrada. Q:2344

nota = int(input())

if nota <= 0:
	print("E")
elif 35 >= nota > 0:
	print("D")
elif 60 >= nota > 35:
	print("C")
elif 85 >= nota > 60:
	print("B")
else:
	print("A")
