def spy_game(nums):
    for i in range (len(nums)):
        if nums[i] == 0:
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    for k in range(j, len(nums)):
                        if nums[k] == 7:
                            return True
    return False
print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))