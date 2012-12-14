
def LP(x):
	n = len(x)
	l =  [[0 for a in range(n+1)] for b in range(n+1)]
	for i in range(n):
		l[i][i] = 1
	for k in range(2,n+1):
		for m in range(n-k+1):
			j = m + k - 1
			if x[m] == x[j]:
				l[m][j] = l[m+1][j-1] + 2
			else:
				l[m][j] = max(l[m][j-1],l[m+1][j])
	print "The length of the longest palindrome subsequence in",x,"is ",l[0][n-1]


LP("ACGTGTCAAAATCG")
LP("MADAM")
LP("ABA")
LP("abacdgfdcaba")
LP("abacdaaadcaba")
LP("CIVIC")
LP("MAHDYNAMICPROGRAMZLETMESHOWYOUTHEM")