
name = 'A'

def printParenthesis(i, j, n, bracket):
    if i == j:
        global name
        print(name,end='')
        name = chr(ord(name)+1)
        return
    
    print("(",end='')
    
    printParenthesis(i, bracket[i][j], n, bracket)
    printParenthesis(bracket[i][j]+1, j, n, bracket)

    print(")",end='')



def matrixChainOrder(p , n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    bracket = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0
    
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i + L - 1
            m[i][j] = 99999999
            for k in range(i,j-1+1):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if q<m[i][j]:
                    m[i][j] = q

                    bracket[i][j] = k

    print("Optimal Parenthesization is : ")
    printParenthesis(1, n - 1, n, bracket)
    print("\nOptimal Cost is : " ,m[1][n - 1])


arr = [40,20,30,10,30]
print(arr)
matrixChainOrder(arr, len(arr))        
