#active cells and inactive cells.
#do refer this link if you have any doubts in question
#https://www.geeksforgeeks.org/active-inactive-cells-k-days/
#ip: [ 1, 0, 0, 0, 1, 0, 1]  (cells of each people)
#    1    (no_of_days)
#    1 - active
#    0 - inactive

#op: [ 0, 1, 0, 1, 0, 0, 0] (after 1 day)

arr = list(map(int, input().split())) # getting array from user
n = len(arr)
k_days = int(input())
for day in range(k_days):
    for i in range(n):
        if i==0:    # for the first cell which has only one neighbour
            ps = arr[i]
            arr[i] = 0 ^ arr[i+1]
        elif i==n-1: # for the last cell which too has only one neigbour
            arr[i] = ps^0
        else:
            ps1 = arr[i]
            arr[i] = ps^arr[i+1]
            ps = ps1
    
print(arr)
