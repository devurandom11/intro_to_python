# Please write an algoritm for the insert_six function that will insert the number "6" into 
# each position of the integer Num and return the largest integer. 
# Do not support the negative numbers, you may handle this case as you see fit. 

# Example input/Output
# input into insert_six(): 20
# Possible positions: 620, 260, 206 ( this line not displayed to user)
# Return 620


# Partial solution inserting character '6'. Still researching how to return max number.
import time

def insert_six(num: int):
    # write your code here
    stringnum = str(num)
    vr = {}
    for i in range (len(stringnum)+1):
        vr[i] = f"{stringnum[:i]}6{stringnum[i:]}"
        time.sleep(.5)
        print (vr[i])
    print()

def main():
    test_numbers = [1, 100, 12345, 65432, 0, -1]
    for num in test_numbers:
        print(f'The number is: {num}\n------------------')
        insert_six(num)

        
if __name__ == "__main__":
    main()
        
