arr= [2, 3, 5, 4, 8]
naam = len(arr)
sum = sum(arr)
mean = sum / naam
no = len(arr)
if no % 2 == 0:
    median1 = arr[no//2]
    median2 = arr[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = arr[no//2]
print(median,mean)
