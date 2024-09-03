### Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para ad
### ireita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas. Vertebrado > ave e
### mamífero ; Ave > carnivoro e onivoro ; Carnivoro > aguia ; Onívoro > pomba ; Mamífero > onivoro e herbivoro ; Onivoro > homem;
### Herbivoro > vaca. Invertebrado > inseto e anelideo ; Inseto > hematofago e herbivoro ; Hematofago > pulga ; Herbivoro > largat
### a ; Anelideo > hematofago e onivoro ; Hematofago > sanguessuga ; Onivoro > minhoca. A entrada contém 3 palavras, uma em cada l
### inha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas. Imprima o nome do animal c
### orrespondente à entrada fornecida. Q:1049

a = input()
b = input()
c = input()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
	animal = 'aguia'

if a == 'vertebrado' and b == 'ave' and c == 'onivoro':
	animal = 'pomba'

if a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
	animal = 'homem'

if a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
	animal = 'vaca'

if a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
	animal = 'pulga'

if a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
	animal = 'lagarta'

if a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
	animal = 'sanguessuga'

if a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
	animal = 'minhoca'

print(animal)
