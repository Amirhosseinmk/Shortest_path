import sys
import networkx as nx
import matplotlib.pyplot as plt
import heapq  # Import heapq for Prim's Algorithm (priority queue)

# Define countries (nodes)
countries = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador",
    "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
]

# Define edges (connections between countries with distances)
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

# Class for Kruskal's Algorithm
class KruskalMST:
    def __init__(self, countries, edges):
        self.countries = countries  # Store the list of countries (nodes) 
        self.edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight (ascending order)  

    def find(self, parent, node):
        if parent[node] != node:  # If node is not its own parent 
            parent[node] = self.find(parent, parent[node])  # Recursively find the root and update  
        return parent[node]  # Return the representative (root) 

    def union(self, parent, rank, node1, node2):
        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)
        if root1 != root2:  # If nodes belong to different sets, merge them 
            if rank[root1] > rank[root2]:  # If root1 has higher rank, make root2 its child  
                parent[root2] = root1
            elif rank[root1] < rank[root2]:  # If root2 has higher rank, make root1 its child 
                parent[root1] = root2
            else:  # If both have the same rank, choose one as the parent and increase its rank  
                parent[root2] = root1
                rank[root1] += 1

    def kruskal_mst(self):
        parent = {country: country for country in self.countries}  # Comprehensive dictionary (keeping track of which node is the leader of its set)
        rank = {country: 0 for country in self.countries}  # Initialize rank of each node as 0
        mst = []
        total_weight = 0

        for country1, country2, weight in self.edges:  # Iterate through sorted edges  
            if self.find(parent, country1) != self.find(parent, country2):  # Check if nodes belong to different sets 
                self.union(parent, rank, country1, country2)  # Merge sets
                mst.append((country1, country2, weight))
                total_weight += weight

        return mst, total_weight

    def visualize_graph(self, edges, title):
        G = nx.Graph()
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G)
        edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3)
        plt.title(title)
        plt.show()

# Class for Prim's Algorithm
class PrimMST:
    def __init__(self, countries, edges):
        self.countries = countries
        self.graph = {country: {} for country in countries}  # Using dictionary for adjacency representation

        for country1, country2, weight in edges:
            self.graph[country1][country2] = weight
            self.graph[country2][country1] = weight  # Adding both directions (undirected graph)

    def prim_mst(self, start):
        mst = []
        total_weight = 0
        visited = set()  # Track visited nodes
        min_heap = [(0, start, None)]  # (weight, current_node, previous_node)

        while len(visited) < len(self.countries) and min_heap:
            weight, current, prev = heapq.heappop(min_heap)  # Get edge with smallest weight

            if current not in visited:
                visited.add(current)
                if prev is not None:
                    mst.append((prev, current, weight))
                    total_weight += weight

                for neighbor, edge_weight in self.graph[current].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor, current))

        return mst, total_weight

    def visualize_graph(self, edges, title):
        G = nx.Graph()
        for edge in edges:
            G.add_edge(edge[0], edge[1], weight=edge[2])

        pos = nx.spring_layout(G, k=1)
        edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}

        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.3)
        plt.title(title)
        plt.show()

# Main Execution
if __name__ == "__main__":
    kruskal = KruskalMST(countries, edges)
    mst_kruskal, total_weight_kruskal = kruskal.kruskal_mst()

    print("\nEdges in the Minimum Spanning Tree (Kruskal's Algorithm):")
    for u, v, weight in mst_kruskal:
        print(f"{u} -- {v} == {weight} km")
    print(f"Total weight of the MST (Kruskal's): {total_weight_kruskal} km")

    prim = PrimMST(countries, edges)
    start_country = input("\nEnter the starting country for Prim's Algorithm: ")

    if start_country not in countries:
        print("Invalid country. Using default: Argentina")
        start_country = "Argentina"

    mst_prim, total_weight_prim = prim.prim_mst(start_country)

    print("\nEdges in the Minimum Spanning Tree (Prim's Algorithm):")
    for u, v, weight in mst_prim:
        print(f"{u} -- {v} == {weight} km")
    print(f"Total weight of the MST (Prim's): {total_weight_prim} km")

    kruskal.visualize_graph(edges, "Original Graph")
    kruskal.visualize_graph(mst_kruskal, "Minimum Spanning Tree (Kruskal's Algorithm)")
    prim.visualize_graph(mst_prim, "Minimum Spanning Tree (Prim's Algorithm)")

