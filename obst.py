def optCost(freq, i, j):
    if j < i:   return 0
    if j == i:  return freq[i]
    Min = 999999999999
    fsum = _Sum(freq, i, j)

    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1) + optCost(freq, r + 1, j))
        if cost < Min: Min = cost
    return Min + fsum

def optimalSearchTree(keys, freq, n):
    return optCost(freq, 0, n - 1)

def _Sum(freq, i, j):
    s=0
    for k in range(i, j + 1):
        s += freq[k]
    return s

keys = [int(item) for item in input("Enter the keys : ").split()]
freq = [int(item) for item in input("Enter the frequencies : ").split()]
n=len(keys) 
print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))
