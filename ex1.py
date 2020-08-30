# solution 1: iteration loop
s = 0
nmax = 1000
for n in range(nmax):
	if n%3 == 0 or n%5 == 0:
		s += n

print(s)

# solution 2: sum of list
ss = sum([m for m in range(nmax) if (m%3 == 0) or (m%5 == 0)])
print(ss)
