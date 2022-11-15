array = [1, 2, 3, 4, 2, 7, 8, 8, 3]
lis=[]
for i in array:
    if i not in lis:
        lis.append(i)
    print(lis)

