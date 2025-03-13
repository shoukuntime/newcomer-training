def check_is_palindrome(x: int) -> bool:
    str_x = str(x)
    str_changed = str_x[::-1]
    if str_x == str_changed:
        return True
    else:
        return False

print(check_is_palindrome(121))
print(check_is_palindrome(-121))
print(check_is_palindrome(10))