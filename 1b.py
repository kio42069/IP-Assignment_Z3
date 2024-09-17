from z3 import *

def find(vertices, edges, weights):
  vertex_vars = [Bool(f"v{i}") for i in range(vertices)]

  edge_weights = [Int(f"w{i}") for i in range(len(edges))]

  s = Solver()
  for i, edge in enumerate(edges):
    s.add(Or(vertex_vars[edge[0]], vertex_vars[edge[1]]))

  for i, edge in enumerate(edges):
    s.add(Implies(And(vertex_vars[edge[0]], vertex_vars[edge[1]]), edge_weights[i] == 1))
    s.add(Implies(Not(And(vertex_vars[edge[0]], vertex_vars[edge[1]])), edge_weights[i] == 0))

  total_weight = Int('total_weight')

  s.add(total_weight >= Sum(edge_weights))

  while s.check() == sat:
    model = s.model()
    vertex_cover = [i for i, v in enumerate(vertex_vars) if model[v]]

    if s.check() == unsat:
      print("No solution found.")
      break

    try:
      total_weight = model.eval(total_weight) # z3 solver automatically finds an efficient vertex cover, we simply need to iterate through all possible solutions 
      print("Vertex cover:", vertex_cover)
      print("Total weight:", total_weight.as_long())  
    except AttributeError:
    # if total weight is None, not sure why this was causing an issue though
      pass
    # this line deletes the current solution and moves on the to next iteration
    s.add(Or([Not(v == model[v]) for v in vertex_vars]))

vertices = 5
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (0, 3), (1, 4), (0, 4)]
weights = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

find(vertices, edges, weights)
