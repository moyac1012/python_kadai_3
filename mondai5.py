n = int(input("何の段を表示しますか？"))

# forの場合
for i in range(1, 10):
    print("{} × {} = {}".format(n, i, n*i))

# whileの場合
i = 1
while i <= 9:
    print("{} × {} = {}".format(n, i, n*i))
    i += 1