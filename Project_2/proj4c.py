# Proj4c: Word Frequency 

# Write a program that reads the contents of a text file. The program should create a dictionary
# in which the keys are the individual words found in the file and the values are the
# number of times each word appears. For example, if the word “the” appears 128 times,
# the dictionary would contain an element with 'the' as the key and 128 as the value. The
# program should either display the frequency of each word or create a second file containing
# a list of each word and its frequency.

# Important: Each word must have punctuation removed (not apostrophe) before further processing. Capitalization should not matter ("The" and "the" are same word.  Words are at least 2 characters or longer.
# Use the following file: Hamlet_2B_or_not_2B.txt

# Constant variable for filename
FILENAME = 'Hamlet_2B_or_not_2B.txt'

# Define main function
def main():
    intro()
    staging_file = read_file(FILENAME)
    # Continue processing file if no errors reading file, else quit. 
    if staging_file == None:
        return None
    elif staging_file != None:
        processed_file = process_file(staging_file)
        final_dictionary = count_words(processed_file)
        print_results(final_dictionary)


# Introduce user to the script.
def intro():
    print('\nWelcome to the Word Frequency App.\nThis app will read the contents of a file and return the number of times each word appears.')
    input('\nPress ENTER to continue...')


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


# Creates an empty dictionary, then uses the get method to assign values to dictionary words (keys).
def count_words(file):
    final_dictionary = {}  # create empty dictionary
    for word in file:
        # Checks if each word is a key in the dictionary. If no, add it and assign value of 1. If yes, add 1 to previous value.
        final_dictionary[word] = final_dictionary.get(word, 0) + 1
    return final_dictionary


# Print dictionary results
def print_results(dictionary):
    print('\nWord\t\tCount')
    print('-'*21)
    for key in dictionary:
        if len(key) < 8:  # Print extra tab for shorter words to make alignment work
            print(f'{key}\t\t{dictionary[key]}')
        else:
            print(f'{key}\t{dictionary[key]}')


# Thank user and prevent auto exit.
def outro():
    print('\nThank you for using the Word Frequency App!\n')
    input('PRESS ENTER TO EXIT')


# Start program
if __name__ == "__main__":
    main()
    outro()
