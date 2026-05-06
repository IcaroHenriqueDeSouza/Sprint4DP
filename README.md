Modelagem do Problema

O fluxo do CRM foi modelado como um grafo direcionado ponderado, onde:
Cada nó representa uma etapa do processo comercial:
Lead, Qualificação, Contato, Proposta, Negociação e Confirmação
Cada aresta representa uma transição possível entre etapas
Cada aresta possui um peso, que representa custo operacional composto, podendo incluir:
tempo médio
esforço da equipe
risco de perda do lead

Algoritmo de Dijkstra

Foi utilizado o algoritmo de Algoritmo de Dijkstra para encontrar o menor caminho entre Lead → Confirmação.
Estratégia:
Uso de fila de prioridade (heapq)
Expansão incremental do menor custo acumulado
Controle de nós visitados para evitar ciclos
Complexidade:
Tempo: O(E log V)
Espaço: O(V)
Propriedades importantes:
Garante caminho ótimo (custos não negativos)
Determinístico quando não há empates de custo
Sensível à modelagem dos pesos

Simulação de Cenários

Foi implementada uma função para simular variações operacionais:
Alteração dinâmica do custo da etapa de negociação
Reexecução do algoritmo para observar impacto no caminho ótimo
Exemplo de cenários:
Processo atual
Negociação com alto custo (ineficiência)
Benefício:
Permite análise de sensibilidade do processo comercial.

Testes

Os testes cobrem diferentes dimensões do problema:
1. Teste Básico
Valida o caminho ótimo esperado
Garante consistência do modelo
2. Caminho Alternativo
Verifica se o algoritmo evita caminhos aparentemente mais curtos, porém mais caros
3. Ausência de Caminho
Garante retorno correto (inf, lista vazia)
4. Presença de Ciclos
Valida que o algoritmo não entra em loop

Pré-requisitos
Python 3.10 ou superior
Biblioteca padrão (heapq)
Decisões de Projeto
Uso de grafo direcionado para representar fluxo real do CRM
Separação entre:
Modelagem (grafo)
Algoritmo (Dijkstra)
Testes
Penalização de caminhos inválidos ao invés de remoção direta
Uso de estrutura simples ao invés de bibliotecas externas

Conclusão

O problema foi resolvido através de:
Modelagem estruturada com grafos
Aplicação do algoritmo de Dijkstra para otimização de fluxo
Ajuste estratégico de pesos para refletir regras de negócio

A solução é:
Determinística
Escalável
Testável
Adaptável a cenários reais

Integrantes do grupo
Ícaro Henrique de Souza Calixto - RM560278
Caio Costa Beraldo - RM560775
Victor Kenzo Mikado - RM560057
Pietro Brandalise De Andrade - RM560142
