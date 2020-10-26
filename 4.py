def can_see_stage(seats):
    res = True
    for i in range(len(seats)):
        if i == 0: continue
        for j in range(len(seats[i])):
            if seats[i][j] <= seats[i-1][j]:
                res = False
    return res

print('can_see_stage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) ->', can_see_stage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print('can_see_stage([[0, 0, 0],[1, 1, 1],[2, 2, 2]]) ->', can_see_stage([[0, 0, 0],[1, 1, 1],[2, 2, 2]]))  
print('can_see_stage([[2, 0, 0],[1, 1, 1],[2, 2, 2]]) ->', can_see_stage([[2, 0, 0],[1, 1, 1],[2, 2, 2]]))
print('can_see_stage([[1, 0, 0],[1, 1, 1],[2, 2, 2]]) ->', can_see_stage([[1, 0, 0],[1, 1, 1],[2, 2, 2]]))