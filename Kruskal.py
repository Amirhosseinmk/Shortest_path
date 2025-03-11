import sys
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush


countries = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
]

edges = [
    ("Argentina", "Bolivia", 1824), ("Argentina", "Brazil", 2239), ("Argentina", "Chile", 1140),
    ("Argentina", "Paraguay", 1002), ("Argentina", "Uruguay", 950), ("Bolivia", "Brazil", 1477),
    ("Bolivia", "Chile", 1702), ("Bolivia", "Paraguay", 1210), ("Bolivia", "Peru", 1086),
    ("Brazil", "Colombia", 2456), ("Brazil", "Guyana", 2460), ("Brazil", "Paraguay", 1331),
    ("Brazil", "Peru", 3012), ("Brazil", "Suriname", 2798), ("Brazil", "Uruguay", 1769),
    ("Brazil", "Venezuela", 2193), ("Chile", "Peru", 2344), ("Colombia", "Ecuador", 1287),
    ("Colombia", "Peru", 1887), ("Colombia", "Venezuela", 1022), ("Ecuador", "Peru", 1324),
    ("Guyana", "Suriname", 285), ("Guyana", "Venezuela", 1536), ("Paraguay", "Uruguay", 1114)
]



class KruskaMST:
    def __init__(self,countries,edges):
        self.countries = countries
        self.edges = sorted(edges, key = lambda x:x[2])
    
    def find(self,parent,node):
        if parent[node] != node:
            parent[node] = self.find(parent,parent[node])
        return parent[node]
    
    def union(self,parent,rank,node1,node2):
        root1 = self.find(parent,node1)
        root2 = self.find(parent,node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    def kruskal_mst(self):
        parent = {country:country for country in self.countries}  #comprehensive dictionary (keeping track of ehich nod is the leader of its set)
        rank = {country : 0 for country in self.countries}
        mst = []
        total_weight = 0

        for country1 ,country2, weight in self.edges:
            if self.find(parent,country1) != self.find(parent,country2):
                self.union(parent,rank,country1,country2)
                mst.append((country1,country2,weight))
                total_weight += weight

        return mst, total_weight

def visualize_graph(self, edges, title):
        G = nx.Graph()
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
        plt.title(title)
        plt.show()



if __name__ == "__main__":
    # Initialize KruskaMST with countries and edges
    kruskal = KruskaMST(countries, edges)

    # Compute the MST
    mst, total_weight = kruskal.kruskal_mst()

    # Display the MST and its total weight
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight} km")
    print(f"Total weight of the MST: {total_weight} km")

    # Visualize the original graph
    visualize_graph(edges, "Original Graph")

    # Visualize the MST
    visualize_graph(mst, "Minimum Spanning Tree (Kruskal's Algorithm)")
