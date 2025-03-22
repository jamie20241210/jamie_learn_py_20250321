try:
    user_weight = float(input("weight ="))
except ValueError:
    print("输入不合理")
except:
    print("except =")
else:
    print("else =", user_weight)
finally:
    print("finally")
