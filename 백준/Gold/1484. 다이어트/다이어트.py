def function(g):
    flag = False
    arr = [i ** 2 for i in range(g // 2 + 2)]
    s = 1
    e = 1
    while e < g // 2 + 2:
        k = arr[e] - arr[s]
        if k == g:
            flag = True
            print(e)
            s += 1
            e += 1
        elif k < g:
            e += 1
        else:
            s += 1
    if flag == False:
        print(-1)
    return


g = int(input())
function(g)