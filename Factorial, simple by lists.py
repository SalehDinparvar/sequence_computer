fac=[1,1] ; n=10
for i in range(n-1):
  fac.append(fac[-1]*len(fac))
print(fac)
