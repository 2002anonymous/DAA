#!/usr/bin/python
# -*- coding: utf-8 -*-
# Recursion approach
# def lcs(X, Y, m, n):

#     if m == 0 or n == 0:
#         return 0
#     elif X[m-1] == Y[n-1]:
#         print(X[m-1],end='')
#         return 1 + lcs(X, Y, m-1, n-1)
#     else:
#         return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

# X = "AGGTAB"
# Y = "GXTXAYB"
# print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )

# Dynamic Programming implementation of LCS problem


def printlcs(X,Y,L,m,n,):
    lcs = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs += X[i - 1]
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = lcs[::-1]
    print('LCS of ' + X + ' and ' + Y + ' is ' + lcs)


def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    print("Length : ",L[m][n])
    printlcs(X, Y, L, m, n)


X = input('Enter X: ')
Y = input('Enter Y: ')
lcs(X, Y)
