n=int(input())
p = input().split()
base = [1, 1]

for i in p :
    
    

    if base[0]==1 and i == 'U' :
        continue
    elif base[1]==1 and i == 'L'    :
        continue
    elif i == 'R'   :
        if(base[1]>=n)   :
            continue
        base[1]+=1
    else :
        if base[0] >= n:
            continue
        base[0]+=1

    
print(base)
