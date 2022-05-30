
def printLIS(arr: list):
	for x in arr:
		print(x, end=" ")
	print()

def constructPrintLIS(arr: list, n: int):
	l = [[] for i in range(n)]
	l[0].append(arr[0])

	for i in range(1, n):
		for j in range(i):
			if arr[i] > arr[j] and (len(l[i]) < len(l[j]) + 1):
				l[i] = l[j].copy()
		l[i].append(arr[i])
	maxx = l[0]
	for x in l:
		if len(x) > len(maxx):
			maxx = x
	printLIS(maxx)

if __name__ == "__main__":

	arr = list(map(int,input("Enter array: ").split()))
	n = len(arr)
	constructPrintLIS(arr, n)

