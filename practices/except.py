try:
    n = int(input("enter num: "))
    d = int(input("enter denum: "))

    res = n/d
    print(res)

    my_list = [1, 2, 3]
    i = int(input("enter index: "))
    print(my_list[i])
except ZeroDivisionError:
    print("denum cant be 0")
except IndexError:
    print("index cannot be greater than list")
finally:
    print("always printed")
print("the end")
