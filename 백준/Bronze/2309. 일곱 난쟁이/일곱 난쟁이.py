arr = [int(input()) for i in range(9)]
arr.sort()

for i in range(8):
    for j in range(i + 1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(arr[k])
            else:
                quit()