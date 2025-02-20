start_num = int(input("開始の数値："))
end_num = int(input("修了の数値："))

if start_num <= end_num:
    while start_num <= end_num:
        print(start_num)
        start_num += 1
else:
    while start_num >= end_num:
        print(start_num)
        start_num -= 1