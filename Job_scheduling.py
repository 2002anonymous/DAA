# greedy approach...
def jobScheduling(a,n,d,job):
    job[0]=0
    job[1]=1
    k=1
    for i in range(2,n+1):
        r = k
        while d[job[r]] > d[i] and d[job[r]]!=r and r>=0: 
            r-=1
        if d[job[r]] <= d[i] and d[i]>r:
            for q in range(r+1, k-1,-1):
                job[q+1] = job[q]
            job[r+1] = i
            k += 1
    return job

if __name__ == '__main__':
    x = [str(s) for s in input("Enter Project Names: ").split()]
    y = [int(s) for s in input("Enter Deadlines: ").split()]
    z = [int(s) for s in input("Enter Profits: ").split()]
    n = len(y)
    a = []
    for i in range(n): a.append([x[i],y[i],z[i]])
    a.sort(key=lambda x:x[2],reverse=True)    
    ids = [i[0] for i in a]
    d = [0]
    for i in range(n): d.append(a[i][1])
    job = [0]*(n+1)

    print('--'*12)
    print('jobId |'.center(6),'Deadline |'.center(10),'Profit'.center(6))
    print('-'*6 + '+' + '-'*10 + '+' + '-'*7)
    for i in a: print(str(i[0]).center(5),'|',str(i[1]).center(8),'|',str(i[2]).center(6))
    print('--'*12)

    job = jobScheduling(a, n, d, job) #function calling....

    print("After Scheduling Jobs:")
    for i in range(1,max([i[1] for i in a])+1): print(i-1,'-',i,end=' | ')
    print('\n','---'*7)
    for i in range(1,max([i[1] for i in a])+1): print(str(ids[job[i]-1]).center(5) if job[i]!=0 else str(0).center(5),end=' | ')