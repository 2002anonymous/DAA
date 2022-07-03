V = 0
INF = 99999
def floydWarshall(graph,x,y):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
	for k in range(V):
		for i in range(V):
			for j in range(V):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	printSolution(dist,x,y)

def printSolution(dist,x,y):
	print("length from ",x," to ",y,":",dist[x][y])

# graph = [[0, 5, INF, 10],
# 		[INF, 0, 3, INF],
# 		[INF, INF, 0, 1],
# 		]

graph = []
while True:
	_graph = list(map(int,input("Enter values of adjacent matrix:").split()))
	graph.append(_graph)
	res = input("Wanna continue? (y/n):")
	if res == "n": break

x,y = tuple(map(int,input("Enter i,j :").split()))
V = len(graph)
floydWarshall(graph,x,y)