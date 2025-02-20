n = int(input("行数を入力してください："))

# forの場合
for i in range(1, n+1):
    print("*"*i)

# whileの場合
i = 1
while i <= n:
    print("*"*i)
    i += 1

# 別解
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()