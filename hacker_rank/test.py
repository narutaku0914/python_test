length_list = []
    for num in set(a):
        if a.count(num) == len(a):
            length_list.append(len(a))
        elif (num + 1) in a:
            length_list.append(a.count(num) + a.count(num + 1))
            
    print max(length_list)