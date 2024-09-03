# Árvore Binária de Busca (Binary Search Tree)
Uma árvore binária de busca é uma árvore binária em que cada nó possui um valor e as seguintes propriedades:
- O valor do nó da esquerda é menor que o valor do nó atual.
- O valor do nó da direita é maior que o valor do nó atual.

## Implementação
A implementação de uma árvore binária de busca pode ser feita de diversas formas, sendo a mais comum a implementação utilizando classes. Cada nó da árvore é uma instância de uma classe que possui um valor e duas referências para os filhos.

## Operações
As operações mais comuns em uma árvore binária de busca são:

### Inserção de um novo nó
Para inserir um novo nó em uma árvore binária de busca, é necessário percorrer a árvore de forma recursiva até encontrar a posição correta para o novo nó. Se o valor do novo nó for menor que o valor do nó atual, a inserção é feita no filho da esquerda. Se o valor do novo nó for maior que o valor do nó atual, a inserção é feita no filho da direita.

### Busca de um nó
Para buscar um nó em uma árvore binária de busca, é necessário percorrer a árvore de forma recursiva até encontrar o nó com o valor desejado. Se o valor do nó atual for igual ao valor desejado, o nó foi encontrado. Se o valor do nó atual for menor que o valor desejado, a busca é feita no filho da direita. Se o valor do nó atual for maior que o valor desejado, a busca é feita no filho da esquerda.
Desta forma, a busca em uma árvore binária de busca é feita de forma eficiente e tem complexidade `O(log n)`, pois a árvore é dividida pela metade a cada nível.

### Remoção de um nó
Para remover um nó de uma árvore binária de bysca, é necessário percorrer a árvore de forma recursiva até encontrar o nó a ser removido. Existem três casos possíveis:
- O nó a ser removido não possui filhos: nesse caso, basta remover o nó da árvore.
- O nó a ser removido possui um filho: nesse caso, basta substituir o nó a ser removido pelo seu filho.
- O nó a ser removido possui dois filhos: nesse caso, é necessário encontrar o nó com o menor valor na subárvore da direita do nó a ser removido. Esse nó é chamado de sucessor e é utilizado para substituir o nó a ser removido. Após a substituição, o nó sucessor é removido da árvore.

### Percursos
Os percursos em uma árvore binária são formas de visitar todos os nós da árvore. Os percursos mais comuns são:
- Pré-ordem: visita o nó atual, o filho da esquerda e o filho da direita.
- Em-ordem: visita o filho da esquerda, o nó atual e o filho da direita.
- Pós-ordem: visita o filho da esquerda, o filho da direita e o nó atual.
- Em largura: visita os nós de cada nível da árvore de cima para baixo e da esquerda para a direita.
