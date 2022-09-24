from email.policy import default

from collections import defaultdict
from turtle import Turtle


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    
    def add_edge(self, src, tgt):
        self.graph[src].append(tgt)

    def breadth_first_search(self, source):
        visited = {source}
        level = {source:0}
        parent = {source: None}
        queue = [source]
        traversal = [source]

        while queue:
            cur = queue.pop()
            print('pop', cur)
            

            for node in self.graph[cur]:
                if node in visited:
                    continue
                print('visiting', node)
                visited.add(node)
                parent[node] = cur
                level[node] = level[cur] + 1
                queue.append(node)
                traversal.append(node)
        
        return traversal, parent, level


    def dfs_helper(self, cur, visited):
        if cur in visited:
            return 
        visited.add(cur)
        print(cur)
        for node in self.graph[cur]:
            self.dfs_helper(node, visited)

    def depth_first_search(self, source):
        visited = set()
        self.dfs_helper(source, visited)
        







