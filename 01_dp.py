def knapSack(points, times, tot_time, tot_que):
    K = [[0 for x in range(tot_time + 1)] for y in range(tot_que + 1)]
    for i in range(tot_que + 1):
        for w in range(tot_time + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif times[i-1] <= w:
                K[i][w] = max(points[i-1] + K[i-1][w-times[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    for i in range(tot_que+1): 
        for j in range(tot_time+1):
            print(str(K[i][j]).zfill(2),end=' ')
            if j==0: print(" | ",end='')
        print()
        if i==0: print('-'*tot_que*7)
    return K[tot_que][tot_time]

# points = [8, 2, 4, 5, 3]
# times = [3, 5, 1, 4, 2]
# tot_time = 10
# tot_que = len(points)

points = list(map(int,input("Enter Points for Each Question:").split()))
times = list(map(int,input("Enter Time for Each Question:").split()))
tot_time = int(input("Enter Total Time:"))
tot_que = len(points)
print("Max Points Earned :",knapSack(points,times,tot_time,tot_que))


'''
n = 3
p = [25, 24, 15]
w = [18, 15, 10]
'''

# import matplotlib.pyplot as p
# import numpy as np
# xpts = [5,15,20,30,40,50,60,70]
# ypts = [0,24,25,40,49,64,64,64]
# p.plot(xpts, ypts)
# p.xlabel("Total time")
# p.ylabel("Maximum Points")
# p.show()
