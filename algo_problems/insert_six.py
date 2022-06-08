# Please write an algoritm for the insert_six function that will insert the number "6" into 
# each position of the integer Num and return the largest integer. 
# Do not support the negative numbers, you may handle this case as you see fit. 

# Example input/Output
# input into insert_six(): 20
# Possible positions: 620, 260, 206 ( this line not displayed to user)
# Return 620


def insert_six(num: int):
    # write your code here
    if num < 0:
        return num
    else:
        stringnum = str(num)
        vr = {}
        for i in range (len(stringnum)+1):
            vr[i] = f"{stringnum[:i]}6{stringnum[i:]}"
        largest_int = max(vr.values())
        return largest_int

def main():
    tests= [20, 9981, 2147483647, 1234565, 0, -1, 8]
    for num in tests:
        print("Largest possible int from {num}: {result}".format(num=num, result=insert_six(num)))
    return

if __name__ == "__main__":
    main()