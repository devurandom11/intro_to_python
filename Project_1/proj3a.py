# Project 3a
# Test Average and Grade:
#
# Write a program that asks the user to enter five test scores. The program
# should display a letter grade for each score and the average test score.
# Write the following functions in the program:
#
# calc_average - This function should accept five test scores as arguments
# and return the average of the scores
#
# determine_grade - This function should accept a test score as an argument and
# return a letter grade for the score based on the following grading scale:
#		Score			Letter Grade
#		-------------------------------------
#		90-100			    A
#		80-89			    B
#		70-79			    C
#		60-69			    D
#		Below 60		    F


# Define main function
def main():

    # Introduce user to script
    intro()

    # Get's user input for 5 test scores.
    score1 = get_score()
    score2 = get_score()
    score3 = get_score()
    score4 = get_score()
    score5 = get_score()

    # Calculate average score
    average_score = calc_average(score1, score2, score3, score4, score5)

    # Determine letter grades for all scores
    grade1 = determine_grade(score1)
    grade2 = determine_grade(score2)
    grade3 = determine_grade(score3)
    grade4 = determine_grade(score4)
    grade5 = determine_grade(score5)
    average_grade = determine_grade(average_score)

    # Print results
    print()
    print(f'\tScores')
    print('-----------------------------')
    print(f'Score 1\t\t{score1:.2f}\t{grade1}')
    print(f'Score 2\t\t{score2:.2f}\t{grade2}')
    print(f'Score 3\t\t{score3:.2f}\t{grade3}')
    print(f'Score 4\t\t{score4:.2f}\t{grade4}')
    print(f'Score 5\t\t{score5:.2f}\t{grade5}')
    print('-----------------------------')
    print(f'Average Score\t{average_score:.2f}\t{average_grade}\n')

    # Thank user and prevent auto exit
    outro()

# Introduces user to script

def intro():
    print('\nWelcome to the Test Average and Grade Calculator.\nThis program will take in 5 test scores and return the letter grades and average test score.\n')

# Get's test score from user. Checks that score is between 0 and 100 and handles errors.

def get_score():
    while True:
        try:
            score = float(input('Please enter a test score: '))
            if 0 <= score <= 100:
                break
            else:
                print('ERROR: Please enter a score between 0 and 100')
        except ValueError:
            print('VALUE ERROR: Please enter a number')
    return score

# Determines letter grade from numeric score

def determine_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

# Calculate average test score from user input

def calc_average(score1, score2, score3, score4, score5):
    average_score = ((score1 + score2 + score3 + score4 + score5) / 5)
    return average_score

# Thank user for using the script and prevent auto exit

def outro():
    print('Thank you for using the Test Average and Grade Calculator App!\n')
    input('PRESS ENTER TO EXIT')


# Start script
if __name__ == "__main__":
    main()
