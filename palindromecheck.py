def palindromecheck(n):
    dummy=n
    rev=0
    while(n>0):
        temp=n%10
        rev=rev*10+temp
        n=n//10

    if(rev==dummy):
        return "palindrome"
    else:
        return "not palindrome"

n=121
print(palindromecheck(n))

