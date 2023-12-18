def palindrome(s):  # check if the string is a palindrome
    return s == s[::-1]


def maxx_palindrome(s):  # find the longest palindrome
    maxx = ''
    for i in range(len(s)):  # go through all substrings and check if they are palindromes
        for f in range(i + 1, len(s) + 1):
            dood = s[i:f]
            if palindrome(dood) and len(dood) > len(maxx):
                maxx = dood
    return maxx


s = input('Enter a string of numbers: ')  # input of the string
result = maxx_palindrome(s)
if s.isdigit() == True:  # check if the string contains only numbers
    print('The longest palindromic string:', result)  # output of the longest palindrome
else:
    print('This string contains not only numbers.')  # output if the string contains not only numbers
    s = input('Enter a string of numbers: ')  # input of the string
