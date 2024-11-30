my_l = [1, 2, 3, 4, 5, 6, 78, 9, 100]
my_l = sorted(my_l)
print(my_l)


# diguishixian1
def foo(index, l):
    if len(l) == 0:
        print("None")
        return
    mid_index = len(l) // 2
    mid_val = l[mid_index]
    if index > mid_val:
        foo(index, l[mid_index + 1 :])
    elif index < mid_val:
        foo(index, l[:mid_index])
    else:
        print("Yes")
        return


foo(5, my_l)
