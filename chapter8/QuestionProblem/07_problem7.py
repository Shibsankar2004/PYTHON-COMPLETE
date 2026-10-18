def rem(l,word):
    n=[]
    for item in l:
     if not(item==word):
        n.append(item.strip(word))
    return n



l=["Shib","sankar","anik","rishi","an","rohan"]

print(rem(l,"an"))