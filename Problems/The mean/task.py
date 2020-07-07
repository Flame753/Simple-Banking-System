def mean():
    num_list = []
    while True:
        num = input()
        if num != ".":
            num_list.append(int(num))
        else:
            break
    return sum(num_list)/len(num_list)


print(mean())
