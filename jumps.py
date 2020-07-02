# https://atcoder.jp/contests/dp/tasks/dp_a
# Frog problem

def frog(N, heights):
    
    if N <= 1:
        return 0
        
    elif N == 2:
        return abs(heights[1] - heights[0])
    elif N == 3:
        return min(abs(heights[2] - heights[0]), (abs(heights[1]-heights[0]) + abs(heights[2]-heights[1])))

    else:
        jump1 = abs(heights[1] - heights[0]) + frog(N-1, heights[1:])
        jump2 = abs(heights[2] - heights[0]) + frog(N-2, heights[2:])
        return min(jump1, jump2)


print("Recursive Solution", frog(2, [10, 10]))
print("Recursive Solution", frog(4, [10, 30, 40, 20]))
print("Recursive Solution", frog(2, [10, 50]))
print("Recursive Solution", frog(6, [30, 10, 60, 10, 60, 50]))
print("Recursive Solution", frog(5, [10, 10, 10, 10, 10]))
print("Recursive Solution", frog(20, [10, 30, 40, 10, 20, 40, 50, 20, 30, 10, 30, 30, 40, 50, 10, 20, 30 ,40 ,50, 20]))


def frog_jump_dp(N, heights):
    cost = []
    ## when N <= 1
    cost.append(0)

    ## when N = 2
    cost.append(abs(heights[1] - heights[0]))

    if N == 2: # 2≤N≤10^5
        return cost[N-1]

    for i in range(2, N):
        jump_type1 = abs(heights[i] - heights[i-1]) + cost[i-1]
        jump_type2 = abs(heights[i] - heights[i-2]) + cost[i-2]
        

        cost.append(min(jump_type1, jump_type2))
        #print(i, jump_type1, jump_type2, cost)
    
    return cost[N-1]

print("DP Solution", frog_jump_dp(2, [10, 10]))
print("DP Solution", frog_jump_dp(4, [10, 30, 40, 20]))
print("DP Solution", frog_jump_dp(2, [10, 50]))
print("DP Solution", frog_jump_dp(6, [30, 10, 60, 10, 60, 50]))
print("DP Solution", frog_jump_dp(5, [10, 10, 10, 10, 10]))
print("DP Solution", frog_jump_dp(20, [10, 30, 40, 10, 20, 40, 50, 20, 30, 10, 30, 30, 40, 50, 10, 20, 30 ,40 ,50, 20]))
