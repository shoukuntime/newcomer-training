def longest_palindrome(s: str) -> str:
    def check_is_palindrome_string(sub_s: str) -> bool:
        sub_s_changed = sub_s[::-1]
        if sub_s_changed == sub_s:
            return True
        else:
            return False
    len_of_s=len(s)
    longest_s=''
    for i in range(len_of_s):
        for j in range(i,len_of_s):
            if check_is_palindrome_string(s[i:j]) and (len(s[i:j])>len(longest_s)):
                longest_s=s[i:j]
    return longest_s

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
