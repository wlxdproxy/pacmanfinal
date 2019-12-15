# Faculdade Área 1 - Wyden  						                                          Salvador-BA 15/12/2019
# Disciplina: Inteligência Artificial
# Professor: Arleys Castro
# Aluno: Wladson Cedraz

 Projeto para implementação de alguns algoritmos de busca:
 - Depth-First Search (DFS)
 - Breadth-First Search (BFS)
 - Uniform-Cost Search (UCS)
 - Search A*
 - FoodSearch

# Questões:
 (Pergunta 1): A ordem de exploração foi de acordo. 
                A busca em profundidade tem o seu custo de execução menor em relação a busca por extensão, 
                porém ela não consegue identificar o caminho mais curto.
                
 (Pergunta 2): Não é uma solução ótima pois a Busca em Profundidade vai sempre percorrer o caminho mais profundo pré-determinado. 
                Suponhamos que a busca percorra primeiro no lado esquerdo, ela vai percorrer os nós até o mais profundo, então se 
                a informação buscada estiver por exemplo em um nó folha ao lado direito da arvore, o algoritmo de busca percorrerá
                primeiro o lado esquerdo inteiro da arvore para só depois analisar o lado direito e chegar até a informação desejada.

 (Pergunta 3): Não é uma solução ótima. Apesar do algoritmo de busca por extensão encontrar o caminho mais curto até o seu objetivo 
                que é a comidinha, ele tem um custo de execução maior por ter que percorrer toda a estrutura para encontrar o caminho
                mais curto.

 (Pergunta 4): No labirinto openMaze nota-se que:
                A busca em profundidade (DFS) teve um custo total de 298, conseguindo alcancar a comida, porem de nao conseguindo 
                encontrar o melhor caminho.
                A busca em largura (BFS) teve um custo total de 54, e conseguiu encontrar o melhor caminho até a comida.

# Bibliografia
 Tech With Tim. Python Path Finding Tutorial - Breadth First Search Algorithm. <https://youtu.be/hettiSrJjM4>. Acessado em: 25/11/2019.
 
 RUSSEL, Stuart. NORVING, Peter. 2013. Inteligencia Artificial
 
 Lenny. Teaching Pacman To Search With Depth First Search. <https://medium.com/@lennyboyatzis/ai-teaching-pacman-to-search-with-depth-first-search-ee57daf889ab>. Acessado em: 02/12/2019.


