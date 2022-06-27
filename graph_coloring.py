
def isSafe(graph, color):
    for i in range(n):
        for j in range(i + 1, n):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True

def graphColoring(graph, m, i, color):
    if (i == n):
        if (isSafe(graph, color)):
            printSolution(color)
            return True
        return False
    for j in range(1, m + 1):
        color[i] = j
        if (graphColoring(graph, m, i + 1, color)):
            return True
        color[i] = 0
    return False

def printSolution(color):
	print("Solution Exists:" " Following are the assigned slots: ")
	for i in range(n):
		print(sbcl[i]+" slot: "+str(color[i]))


n=int(input("Enter no.of subjects:"))
l=[]
sbcl=[]
graph=[[0]*n for i in range(n)]
for i in range(n):
    sbc=str(input("Enter subject code:"))
    sbn=str(input("Enter subject name:"))
    l.append(i)
    sbcl.append(sbc)

my_dict=dict(zip(sbcl,l))
for i in range(n):
    for j in range(i,n):
        v=int(input("Enter 1 if "+sbcl[i]+" clashes with "+sbcl[j]+" else enter 0:"))
        graph[my_dict.get(sbcl[i])][my_dict.get(sbcl[j])]=v
        graph[my_dict.get(sbcl[j])][my_dict.get(sbcl[i])]=v
m = n-1
color = [0 for i in range(n)]
if (not graphColoring(graph, m, 0, color)):
    print ("Solution does not exist")