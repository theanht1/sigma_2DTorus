# Convert edges
f_edges_in = open("sw_2DTorus2_n64_r2.edges", "r")
f_edges_out = open("edges", "w")

edges_str = f_edges_in.read()
edges_str = edges_str.split("\n")
edges_str.pop()
numOfEdge = len(edges_str)
edges = []
for i in range(0, numOfEdge):
	edges.append(edges_str[i].split(" "))

f_edges_out.write("var numOfEdge = " + str(numOfEdge) + ";\n")
f_edges_out.write("var edges = [\n")

for i in range(0, numOfEdge):
	f_edges_out.write("[" + str(edges[i][0]) + ", " + str(edges[i][1]) + "],\n")
f_edges_out.write("];\n")
f_edges_out.close()

# Convert geo
f_geo_in = open("sw_2DTorus2_n64_r2.geo", "r")
f_geo_out = open("geos", "w")

f_geo_in.readline()
geos_str = f_geo_in.read()
# print(geos)
geos_str = geos_str.split("\n")
geos_str.pop()
numOfVertex = len(geos_str)
geos = []
for i in range(0, numOfVertex):
	geos.append(geos_str[i].split(" "))

f_geo_out.write("var numOfVertex = " + str(numOfVertex) + ";\n")
f_geo_out.write("var geos = [\n")
for i in range(0, numOfVertex):
	f_geo_out.write("[" + str(geos[i][0]) + ", " + str(geos[i][1]) + ", " + str(geos[i][2]) +  "],\n")
f_geo_out.write("];\n")
f_geo_out.close()
