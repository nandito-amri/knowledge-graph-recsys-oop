import networkx as nx

class Graph:
  def __init__(self, edges_list, columns, file_path):
    self.edges_list = edges_list
    self.columns = columns
    self.file_path = file_path
    self.graph = self._create_graph()

  def _create_graph(self):
    return nx.from_pandas_edgelist(self.edges_list, self.columns[0], self.columns[1], self.columns[2])
  
  def save_graph(self):
    nx.write_graphml_lxml(self.graph, self.file_path)

  def get_triplets(self):
    triplets = [(u, self.graph[u][v]['relation'], v) for u, v in self.graph.edges]
    return triplets
