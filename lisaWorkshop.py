def workbook(n,k,arr):

    special_problems = 0
    page_number = 1


    for i in range(0, n):
        for j in range(1, arr[i]+1):
            if j == page_number:
                special_problems += 1
            if j == i or j % k == 0:
                page_number += 1

    return special_problems

arr = [4,2,6,1,10]
print(workbook(5,3,arr))
