start_num = int(input("開始の数値："))
end_num = int(input("修了の数値："))

# forを使うパターン
for i in range(start_num, end_num+1):
    print(i)

# whileを使うパターン
while start_num <= end_num:
    print(start_num)
    start_num += 1