def op(a,k,i):
    if i<=k:
        a=str(a)
        b=a[::-1]
        if a==b:
            return [i,int(a)]
        else:
            a=int(a)+int(b)
            i+=1
            return op(a,k,i)
    else:
        return [-1,-1]
        
a=int(input())
k=int(input())
print(op(a,k,0))
