from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)
		self.Time = 0
		self.count = 0

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def BCCUtil(self, u, parent, low, disc, st):
		children = 0
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1
		for v in self.graph[u]:
			if disc[v] == -1 : 
				parent[v] = u
				children += 1
				st.append((u, v)) 
				self.BCCUtil(v, parent, low, disc, st)
				low[u] = min(low[u], low[v])
				if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
					self.count += 1 
					w = -1
					while w != (u, v):
						w = st.pop()
						print(w,end=" ")
					print()
			
			elif v != parent[u] and low[u] > disc[v]:
				low[u] = min(low[u], disc[v])
	
				st.append((u, v))

	def BCC(self):
		disc = [-1] * (self.V)
		low = [-1] * (self.V)
		parent = [-1] * (self.V)
		st = []
		for i in range(self.V):
			if disc[i] == -1:
				self.BCCUtil(i, parent, low, disc, st)
			if st:
				self.count = self.count + 1

				while st:
					w = st.pop()
					print(w,end=" ")
				print ()

vertices = int(input("Enter no of vertices in graph: "))
g = Graph(vertices)
print("keep Entering Edges in pairs and exit with -1,-1")
while True:
	x,y = tuple(map(int,input("Enter edges: ").split()))
	g.addEdge(x, y)
	if x == -1 and y == -1: break

g.BCC()
print (f"Above are {g.count} biconnected components in graph")


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0,1,2,3,4,5,6,7])
# ypoints = np.array([1,2,4,5,7,9,11,15])

# plt.plot(xpoints, ypoints)
# plt.xlabel("Articulation points in graph")
# plt.ylabel("Number of Bi-connected components")
# plt.show()

