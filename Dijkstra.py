from bubble_sort import bubbleSort
import sys

def dijkstra(graph, src):
    inf = sys.maxsize  #Representing infinity
    node_data = {country : {'cost':inf, 'pred':[]} for country in graph}  #initially, each node has this information of Cost : infinity and predicessors
    node_data[src]['cost'] = 0 #this is the cost of source which is 0 (starting from itself to itself)

    visited = [] #list of the visited node
    
    while len(visited) < len(graph): #repeating until we have visited all countries , so this loop continue runs as long as there are countries we have not visited
        min_country = None #we need to find the country with smallest distance
        min_cost = inf #it means minimum cost has not been updated
        for country in node_data:
            if country not in visited and node_data[country]['cost'] < min_cost: #so if the country's distance was smaller than min cost (at first pace infinit)
                min_cost = node_data[country]['cost'] #update min cost and min country
                min_country = country #updating the min_country
                if min_country is None: #this means we have reached all posible destination 
                    break
                visited.append(min_country) #append the min_country to visited list , we won't process it again
                for neighbor, distance in graph[min_country].items(): #for neighbors and its distance extract their prices
                    if neighbor not in visited:
                        new_cost = node_data[min_country]['cost'] + distance
                        if new_cost < node_data[neighbor]['cost']:
                            node_data[neighbor]['cost'] = new_cost
                            node_data[neighbor]['pred'] = min_country
    return node_data



graph = {
    'Argentina':{'Bolivia':1824,'Brazil':2239, 'Chile':1140,'Paraguay':1002,'Uruguay':950},
    'Bolivia':{'Argentina':1824,'Brazil':1477,'Chile':1702,'Paraguay':1210, 'Peru':1086},
    'Brazil':{'Argentina':2239,'Bolivia':1477,'Colombia':2456 , 'Guyana':2460, 'Paraguay':1331,'Peru':3012, 'Suriname':2798, 'Uruguay':1769, 'Venezuela':2193},
    'Chile': {'Bolivia':1702,'Argentina':1140,'Peru':2344},
    'Colombia':{'Brazil':2456,'Ecuador':1287,'Peru':1887,'Venezuela':1022},
    'Ecuador':{'Colombia':1287,'Peru':1324},
    'Guyana':{'Brazil':2460,'Suriname':285,'Venezuela':1536},
    'Paraguay':{'Brazil':1331,'Bolivia':1210,'Argentina':1002,'Uruguay':1114},
    'Peru': {'Bolivia':1086,'Brazil':3012,'Chile':2344,'Colombia':1887,'Ecuador':1324},
    'Uruguay':{'Argentina':950,'Brazil':1769,'Paraguay':1114},
    'Suriname':{'Brazil':2798,'Guyana':285},
    'Venezuela':{'Brazil':2193,'Colombia':1022,'Guyana':1536}
}

#here you can write the name of any country and get shortest paths and their corresponding distances
source = input("Enter the starting country: ")

if source not in graph:
    print("The country you enter is not in the graph")
result = dijkstra(graph,source)




print("\nShortest paths from", source)
print("-" * 40)
print(f"{'Country':<15}{'Cost (km)':<15}{'Predecessor'}")
print("-" * 40)

sorted_result = bubbleSort(list(result.items()), key = lambda x:x[1]['cost'])

for country , data in sorted_result:
    pred = data['pred'] if data['pred'] else "None"
    print(f"{country:<15}{data['cost']:<15}{pred}")
