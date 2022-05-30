Max=1000
def permutation(l):
    if len(l)==0:
         return []
    elif len(l)==1:
         return [l]
    else:
         Lt=[]
 
         for i in range(len(l)):
             m=l[i]
             remList=l[:i]+l[i+1:]
             for p in permutation(remList):
                 Lt.append([m]+p)
    return Lt
def tsp(graph,s,V):
    vertex=[]
    tour=''
    for i in range(V):
        if i!=s:
            vertex.append(i)

    min_path=Max
    next=permutation(vertex)
    t=0
    path=[]
    tour=[]
    for i in next:
        curr_wt=0
        k=s
        loc=str(s+1)+' '
        for j in i:
           curr_wt+=graph[k][j]
           k=j
           loc+=str(k+1)+' '
        curr_wt+=graph[k][s]
        loc+=str(s+1)+' '
        path.append(curr_wt)
        tour.append(loc)
        t+=1
    j=0
    min=path[0]
    for i in range(t):
        m=path[i]
        if m<min:
            m=min
            j=i
    t=tour[j].split()
    t=list(map(int,t))
    p=''
    for i in range(len(t)-1,0,-1):
        p+=str(t[i])+'->'
    p+=str(t[0])
    return path[j],p
v=int(input('No.of objects: '))
graph=[]
print('Enter slewing time for travel from each object to all other objects along with current to starting one')
for i in range(v):
   l=input('{}--'.format(i+1))
   l=list(map(int,l.split()))
   graph.append(l)
s=0
time,tour=tsp(graph,s,v)
print('The minimum total slewing time is',time)
print('The tour of the satellite is',tour)