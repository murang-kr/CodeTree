N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
def in_arr(x, y):
    return x >= 0 and y >= 0 and x < N and y < M

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            if in_arr(i, j-2) and arr[i][j-1] == "E" and arr[i][j-2] == "E": #west
                cnt += 1 
            
            if in_arr(i, j+2) and arr[i][j+1] == "E" and arr[i][j+2] == "E": #east
                cnt += 1
            
            if in_arr(i-2, j) and arr[i-1][j] == "E" and arr[i-2][j] == "E": #north
                cnt += 1 

            if in_arr(i+2, j) and arr[i+1][j] == "E" and arr[i+2][j] == "E": #south
                cnt += 1
            
            if in_arr(i-2, j-2) and arr[i-1][j-1] == "E" and arr[i-2][j-2] == "E": #northwest
                cnt += 1 

            if in_arr(i-2, j+2) and arr[i-1][j+1] == "E" and arr[i-2][j+2] == "E": #northeast
                cnt += 1 

            if in_arr(i+2, j-2) and arr[i+1][j-1] == "E" and arr[i+2][j-2] == "E": #southwest
                cnt += 1 
            
            if in_arr(i+2, j+2) and arr[i+1][j+1] == "E" and arr[i+2][j+2] == "E": #southeast
                cnt += 1 

print(cnt)