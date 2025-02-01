def has_33(nums):
    for i in range (len(nums) - 1):
        if nums[i] == 3 and nums[i + 1]== 3:
            return(True)
    return(False)
def unique(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)
def histogram (lst):
    for x in lst:
        print ("*" * x)