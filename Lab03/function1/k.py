def palindrome(lst):
    reverse = lst[::-1]
    if lst == reverse:
        print("It is palindrome")
    else :
        print("It is not palindrome ")
palindrome("madam")