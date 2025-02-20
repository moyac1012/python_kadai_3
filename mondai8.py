n = int(input("行数を入力してください："))

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)