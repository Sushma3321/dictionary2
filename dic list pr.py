a={'1':['a','b'], '2':['c','d']}
i=0
while i<len(a):
    c=a['1']
    d=a['2']
    e=[c,d]
    i=i+1
j=0
while j<len(e):
    k=0
    while k<len(e[j]):
        print(e[0][j],e[1][k])
        
        k=k+1
       
    j=j+1

