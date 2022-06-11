# Lab7: Unique Words
#
# Write a program that opens a specified text file then displays a list of 
# all the unique words found in the file.  HINT: "The" and "the" are the same 
# word, and store each word as an element of a set.
# 
# Use the following file: Hamlet_2B_or_not_2B.txt
# 
# Use comments and good variable names. Save your Python script as Lab7.py

# Constant variable for filename
FILENAME = 'Hamlet_2B_or_not_2B.txt'

# Define main function
def main():
    intro()
    staging_file = read_file(FILENAME)
    # Continue if staging_file() function didn't have errors, else exit. 
    if staging_file == None:
        return None
    elif staging_file != None:
        processed_file = process_file(staging_file)
        final_set = count_words(processed_file)
        print_results(final_set)
    

# Introduce user to the script.
def intro():
    print('\nWelcome to the Unique Word App.\nThis app will read the contents of a file and return the unique words in the file.\n')
    input('Press ENTER to continue...')


# Opens file, reads contents, closes file. Program gives warning and exits on IOError.
def read_file(file):
    try:
        in_file = open(file, 'r')
        staging_file = in_file.read()
        in_file.close()
        return staging_file
    except IOError:
        print('\nERROR: FILE NOT FOUND.\n\nPlease run this program from the directory containing the file \'Hamlet_2B_or_not_2B.txt\'.')
        return None
    

# Removes extra characters, new-line characters, and splits contents into individual words.
def process_file(file):
    processed_file = file.lower().replace(':', '').replace(';', '').replace(',', '').replace('!', '').replace('?', '').replace(
        '.', '').replace('-', ' ').rstrip('\n').split()  # Is this one-liner okay or is it better to have more lines?
    return processed_file

# Creates an empty set, then uses the get method to assign values to set words (keys).
def count_words(file):
    final_set = set()  # create empty set
    for word in file:
        final_set.add(word)
    return final_set

# Print results
def print_results(final_set):
    print('\nWords')
    print('-'*10)
    for items in final_set: # Print items line by line instead of as a set.
        print(items) 


# Thank user and prevent auto exit.
def outro():
    print('\nThank you for using the Word Frequency App!\n')
    input('PRESS ENTER TO EXIT')


# Start program
if __name__ == "__main__":
    main()
    outro()
