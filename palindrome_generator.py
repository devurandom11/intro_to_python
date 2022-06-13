import time

def palindrome_locator():
    palindromes=[]


    for count in range(333333333):
        n = str(count)
        if n == n[::-1]:
            palindromes.append(n)

    for num in palindromes:
        for i in range(int(num) + 1):
            cube = i*i*i
            if (cube == int(num)):
                print(f"Hooray! {num} is a palindromic cube!")
#                time.sleep(.1)
           # else:
            #    print(f"{num} IS NOT A CUBE")  
#                time.sleep(.1)
if __name__=="__main__":
    palindrome_locator()