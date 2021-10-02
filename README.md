# Estrutura de dados em Python
## Lista Ligada
* Uma **lista ligada** ou lista encadeada é uma estrutura de dados linear e dinâmica. Ela é composta por **células que apontam para o próximo elemento da lista**. Para "ter" uma lista ligada/encadeada, basta guardar seu primeiro elemento, e seu último elemento aponta para uma célula nula. O esquema a seguir representa uma lista ligada/encadeada com 5 elementos:
* Célula 1 ---> Célula 2 ---> Célula 3 ---> Célula 4 ---> Célula 5 ---> (Nulo)
* Para inserir dados ou remover dados é necessário ter um ponteiro que aponte para o 1º elemento e outro que aponte para o fim, porque se queremos inserir ou apagar dados que estão nessas posições, a operação é rapidamente executada. Caso seja necessário editar um nó que esteja no meio da lista haverá uma busca pela posição desejada.
## Lista Duplamente Ligada
* Uma **lista duplamente ligada** ou lista duplamente encadeada é uma estrutura de dados ligada que consiste de um conjunto de registros sequencialmente ligados chamados de **nós** e é uma extensão da lista simplesmente ligada. Cada nó contem **dois campos**, chamados de links ou enlaces, que são referências para o **nó anterior e para o nó posterior** na sequência de nós. Os links anteriores e posteriores dos nós inicial e final, respectivamente, apontam para algum tipo de terminador, tipicamente um nó sentinela ou nulo, para facilitar o percorrimento da lista. Se houver apenas um nó sentinela, a lista será vinculada circularmente através do nó sentinela. Ele pode ser conceituado como duas listas unicamente vinculadas formadas a partir dos mesmos itens de dados, mas em ordens sequenciais opostas.


![](https://github.com/DarlanNoetzold/Estrutura_de_Dados/blob/main/ldl.png)

## Fila
* Uma **fila** é uma estrutura de dados dinâmica que admite remoção de elementos e inserção de novos objetos.  Mais especificamente, uma  fila  (= queue)  é uma estrutura sujeita à seguinte regra de operação:  sempre que houver uma remoção, o elemento removido é o que está na estrutura há mais tempo. Em outras palavras, o primeiro objeto inserido na fila é também o primeiro a ser removido. Essa política é conhecida pela sigla **FIFO** (= First-In-First-Out).
## Pilha
* Uma pilha é uma estrutura de dados que admite remoção de elementos e inserção de novos objetos.  Mais especificamente, uma  pilha (= stack)  é uma estrutura sujeita à seguinte regra de operação:  sempre que houver uma remoção, o elemento removido é o que está na estrutura há menos tempo. Em outras palavras, o primeiro objeto a ser inserido na pilha é o último a ser removido. Essa política é conhecida pela sigla **LIFO** (= Last-In-First-Out).
## Árvore
* Uma **árvore** é formada por um conjunto de elementos que armazenam informações chamados **nodos**. Toda a árvore possui o elemento chamado **raiz**, que possui ligações para outros elementos denominados **ramos ou filhos**. Estes ramos podem estar ligados a outros elementos que também podem possuir outros ramos. O elemento que não possui ramos é conhecido como **nó folha**, nó terminal ou nó externo

---

⭐️ From [DarlanNoetzold](https://github.com/DarlanNoetzold)
