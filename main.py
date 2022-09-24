from graph import Graph

g = Graph()
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('b', 'c')
g.add_edge('c', 'a')
g.add_edge('c', 'd')
g.add_edge('d', 'd')

# print(g.breadth_first_search('c'))
print(g.depth_first_search('c'))