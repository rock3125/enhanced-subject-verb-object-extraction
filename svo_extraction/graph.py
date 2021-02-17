import networkx as nx
import matplotlib.pyplot as plt
class SVONetwork():
    def __init__(self, svos:"list of tuples where each tuple has the subject, verb, object, example [('bees','produce','honey')]"):
        self.svos = svos

    def createSVOGraph(self, direction:"direct|indirect, default indirect"="indirect", save_image=True, name_image="", display_grap=True):
        G = None
        if direction == "direct":
            G = nx.DiGraph(day="directsvo")
        elif direction=="indirect":
            G = nx.Graph(svo="indirectsvo")
        else:
            raise ValueError("direct parameters just accepts direct and indirect as value")

        for subject, verb, object in self.svos:
            if not object:
                continue

            if subject not in G:
                G.add_node(subject, text=subject, svotype="subject")

            if object not in G:
                G.add_node(object, text=object, svotype="object")

            G.add_edge(subject, object,text=verb)

        if display_grap:


            pos = nx.spring_layout(G)
            edge_labels = nx.get_edge_attributes(G, 'text')
            nx.draw_networkx_edge_labels(G,pos=pos, edge_labels=edge_labels)
            nx.draw(G, pos=pos,with_labels=True)
            if save_image:
                if not name_image:
                    raise ValueError("if save_image is true then name_image is required, it could be a name or a path with the name")
                else:
                    plt.savefig(name_image)

            plt.show()
        return G



