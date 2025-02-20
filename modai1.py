name = input("名前：")
age = int(input("年齢："))

if age >= 20:
    print(name + "さんはお酒が飲めます")
    # print("{}さんはお酒が飲めます".format(name))  # こっちでもOK
else:
    print(name+ "さんはまだ飲めません")
    # print("{}さんはまだ飲めません".format(name))  # こっちでもOK
    

