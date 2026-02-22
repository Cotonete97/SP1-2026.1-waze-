#"for x in y" pega cada item 1 por 1 que está em y e coloca um por um dentro do x

grafo = { #Defini uma variável chamada "grafo" que representa um grafo hipotético e armazena um dicionario ("{}" define um dicionario em python, que é uma tabela que liga uma chave a um valor)
    "A": {"B": 4, "C": 2}, # "A" é uma stringVizinhos de A são: B( custo 4 de A até B) e C(custo 2 de A até C). Chave "B" equivale ao valor "4"
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}

inicio = "A"
destino = "E"

def dijkstra(grafo_recebido, inicio, destino=None): #"def" é o comando para criar função. Os parametros receberam valores apenas quando a função for chamada
    infinito = float("inf") #Criei uma variável chamada "infinito" e atribui o valor infinito do tipo float a ela

    dist = {} # dicionário vazio que vai guardar as distâncias com menor custo no futuro
    prev = {} # dicionário vazio que vai guardar o nó de menor custo do caminha anterior

    for no in grafo_recebido: #Pega tudo o que está em "grafo_recebido" e coloca 1 por 1  em "no". No caso, passa 1 por 1 pelas chaves de grafo_recebido e coloca em nó
        dist[no] = infinito
        prev[no] = None

    dist[inicio] = 0 #Distancia de A=0 porque já estamos em A

    nao_processados = set() #Crir uma variável chamada "nao_processados" e torna ela um conjunto vazio
    for no in grafo_recebido:
        nao_processados.add(no) #adiciona os nós em "nao_processados", representando os nós que ainda não foram analisados pelo dijkstra

    while len(nao_processados) > 0: #Enquanto o tamanho dos "nao_processados" for positivo, continua. Isso faz com que o dijkstra veja todos os nós

        atual = None #nó atual que está sendo processado
        menor_custo = infinito #começa com isso, mas futuramente vai ser crrigido para o valor que encontrarmos

        for no in nao_processados: #percorre todos os nós não processados
            if dist[no] < menor_custo: #acha qual dos nós tem o menor custo
                menor_custo = dist[no]
                atual = no #guarda o melhor nó em "atual"

        if atual is None or dist[atual] == infinito:
            break #se o nó ainda continuou sendo infinito, nãoé alcançavel

        if destino is not None and atual == destino:
            break #Se existe um destino definido E o nó atual já é o destino, então pare o algoritmo

        for vizinho in grafo_recebido[atual]:
            peso = grafo_recebido[atual][vizinho]

            if peso < 0:
                raise ValueError("Dijkstra não aceita pesos negativos.")

            novo_custo = dist[atual] + peso 

            if novo_custo < dist[vizinho]: #Atualiza o melhor custo conhecido
                dist[vizinho] = novo_custo
                prev[vizinho] = atual  #Salva o “pai / predecessor” do vizinho

        nao_processados.remove(atual) #"“Esse nó já foi processado e está finalizado. Não preciso olhar ele de novo.”"

    return dist, prev #return é quem devolve valores para quem chamou a função. No caso: "dist"(melhores custos) e "prev"(predecessores (pais) para reconstruir o melhor caminho)


def reconstruir_caminho(prev, inicio, destino):
    caminho = []
    atual = destino #começa do destino para voltar “de trás pra frente”

    while atual is not None:
        caminho.append(atual) #"append" é para adicionar ao final da lista.

        if atual == inicio:
            break

        atual = prev[atual] #Anda para trás refazendo o caminho

    caminho.reverse()

    if len(caminho) == 0 or caminho[0] != inicio:
        return []

    return caminho

dist, prev = dijkstra(grafo, inicio, destino=destino) #Aqui se executa de fato
caminho = reconstruir_caminho(prev, inicio, destino)

print("Custo mínimo:", dist[destino]) 
print("Caminho:", " -> ".join(caminho)) #join junta itens de uma lista de textos com um separador.
