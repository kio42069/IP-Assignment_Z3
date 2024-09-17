from z3 import *

def find_vertex_cover(edges):
  vertices = calc_vertices(edges)
  vertex_vars = [Bool(f"v{i}") for i in range(vertices)]
  s = Solver()
  for edge in edges:
    s.add(Or(vertex_vars[edge[0]], vertex_vars[edge[1]]))

  if s.check() == sat:
    model = s.model()
    vertex_cover = [i for i, v in enumerate(vertex_vars) if model[v]]
    print(vertex_cover)
  else:
    print("no vertex cover")

def calc_vertices(edges):
    vertices = []
    for i in edges:
        vertices.append(i[0])
        vertices.append(i[1])
    vertices = len(set(vertices))
    return vertices
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (0, 3), (1, 4), (0, 4)]

find_vertex_cover(edges)
