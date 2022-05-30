n = int(input("No of items : "))
m = int(input("Capacity of bag : "))
p = list(map(int, input("Enter profits : ").split()))
w = list(map(int, input("Enter weights : ").split()))
q = {p[i]:w[i] for i in range(n)}
d = {}
res = 0
print("\nWeights are their Ratio's: ")
print("-"*10)
for i in range(n):
    d[p[i]/w[i]] = p[i]
    print(w[i], " ", round(p[i]/w[i],2))

d = {k : v for k,v in sorted(d.items(), reverse= True)}
for k,v in d.items():
    if(q[v] <= m):
        m = m - q[v]
        res += v
    else:
        res += ((m/ q[v])*v)
        break
print("\nThe Maximum Profit: {}".format(res))
