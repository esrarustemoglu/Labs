def unique(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)
my_list = [1, 2, 3, 1, 4, 5, 3]
unique(my_list)