arr = [list(map(int, input().split())) for _ in range(2)]
print(f"{sum(arr[0])/len(arr[0]):.1f} {sum(arr[1])/len(arr[1]):.1f}")
print(f"{(arr[0][0]+arr[1][0])/2:.1f} {(arr[0][1]+arr[1][1])/2:.1f} {(arr[0][2]+arr[1][2])/2:.1f} {(arr[0][3]+arr[1][3])/2:.1f}")
print(f"{(sum(arr[0])+sum(arr[1]))/8:.1f}")