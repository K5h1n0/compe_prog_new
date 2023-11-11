p,q = input().split()
alph = "A__BC___DE____F________G"
pidx = alph.find(p)
qidx = alph.find(q)
print(abs(pidx-qidx))