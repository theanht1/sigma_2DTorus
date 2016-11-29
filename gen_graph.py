from random import randint

nRow = 8
nCol = 8
nNode = nRow * nCol

f_geos = open("sw_2DTorus2_n64_r2.geo", "w")
f_geos.write("T_" + str(nNode) + "_" + str(nRow) + "_" + str(nCol) + "\n")

for i in range(0, nNode):
  f_geos.write(str(i) + " " + str(i % nCol) + " " + str(int(i / nCol)) + "\n")

f_geos.close()


f_edges = open("sw_2DTorus2_n64_r2.edges", "w")

edges = []
degree = [0] * nNode

def inEdges(source, target):
  return ((source, target) in edges) or ((target, source) in edges)

def nodeIndex(row, col):
  return row * nRow + col

def addEdges(source, target):
  if not inEdges(source, target):
    edges.append((source, target))
    degree[source] += 1
    degree[target] += 1


for i in range(0, nNode):
  row = int(i / nCol)
  col = i % nCol

  ## Add edges with neighbour nodes
  if row > 0:
    addEdges(i, nodeIndex(row - 1, col))

  if row < nRow - 1:
    addEdges(i, nodeIndex(row + 1, col))

  if col > 0:
    addEdges(i, nodeIndex(row, col - 1))

  if col < nCol - 1:
    addEdges(i, nodeIndex(row, col + 1))

  ## Add random edges  
  count = 0
  while degree[i] < 6  and count < 1000000:
    j = randint(0, nNode - 1)
    
    while j == i or degree[j] >= 6 or inEdges(i,j) and count < 100000:
      count += 1
      j = randint(1, nNode - 1)

    # print(i,j)
    addEdges(i, j)
  
# print(len(edges))
# print(edges[0][0])
for i in range(0, len(edges)):
  f_edges.write(str(edges[i][0]) + " " + str(edges[i][1]) + "\n")
f_edges.close()
