import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, label):
    # create directed networkx graph
    G = nx.Graph()

    # add edges
    G.add_edges_from(graph)
    # graph_pos = nx.shell_layout(G)
    # graph_pos = nx.spectral_layout(G)
    #graph_pos = nx.spring_layout(G)
    graph_pos = nx.random_layout(G)

    # draw nodes, edges and labels
    nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)

    # we can now added edge thickness and edge color
    nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=label)

    plt.show()
#['Congressional Research', 'Institute', 'Science', 'International', 'North Korea', 'ICBM', 'ICBM']
    
    
entity = [['Radeon RX Vega', 'Bethesda', 'Less', 'Rapid Pack Math', 'Nvidia', 'Ryzen', 'Deus Ex', 'Vega', 'Mankind Divided', 'Tomb Raider', 'Nvidia Pascal', 'Memory', 'Lara Croft', 'Cache Controller', 'Raja Koduri', 'Star Wars Battlefront', 'Vega GPUs', 'Radeon Instict'], ['Whitehaven', 'Stay', 'Ryzen Enthusiast', 'Vega', 'Radeon RX Vega GPU', 'Ryzen CPUs'], ['Nvidias GPU', 'Radeon RX Vega', 'Vega'], ['Bethesdas', 'Star Wars', 'Radeon RX Vega', 'Radeon RX', 'Radeon RX Vega Graphics Card Packaging Leaked', 'Titan Xp', 'Quake Champions', 'Radeon Chill', 'Battlefront', 'Id Tech', 'Card Packaging Pictured Supposedly', 'Vega GPUs', 'Card', 'Radeon'], ['Radeon RX Vega', 'Scott Herkelman', 'Herkelman', 'Mr.', 'Vega', 'Scott', 'Fiji'], ['Hynix'], ['High Bandwidth Cache Controller', 'Koduri', 'Rapid', 'Vega GPU', 'Raja', 'Cache Controller Raja Koduri', 'Deus Ex Mankind Divided', 'Vega AMD Vega', 'Vega', 'Radeon Virtualized Encoding', 'Advanced Pixel Engine', 'Cache Controller', 'Geometry Pipeline'], ['Polaris', 'Radeon'], ['Radeon RX', 'Radeon RX Vega', 'Scott Herkelman']]
graph = []
label = {}
temp = {}
for item in entity:
    for i in item:
        for j in item:
            if i != j:
                val = (i, j)
                if val in temp:
                    temp[val] = temp[val] + 1
                    if temp[val] > 1:
                        label[val] = temp[val]
                        graph.append(val)
                else:
                    temp[val] = 1

draw_graph(graph, label)

