n = int(input("合計を取りたい数："))

# forの場合
count = 0
for i in range(1,n+1):
    count += i
print(count)

# whileの場合
i = 1
count = 0
while i <= n:
    count += i
    i += 1
print(count)
