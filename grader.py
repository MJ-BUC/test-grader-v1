'''
This is a program that grades tests from a text file and outputs
the first name, last name, test score, and letter grade to a 
new text file. Version 1
'''

TEST_ANSWERS = 'test_answers.txt'
GRADED_TESTS = 'graded_tests.txt'
CORRECT = 5
INCORRECT = .25


def letter_grade(score):
    #Determines the grade of associated with the core that is
    #passed as an argument and returns the grade.
    if score >= 90:
        grade = 'A'

    elif score >= 80 and score < 90:
        grade = 'B'

    elif score >= 70 and score < 80:
        grade = 'C'

    elif score >= 60 and score < 70:
        grade = 'D'

    else:
        grade = 'F'

    return grade


def calculate_score(score, formatted_answers, answer_key, index_counter1, index_counter2):
    #Calculates the score by looping over each answer in the list
    #and returns the score and counter.
    for ch in answer_key:
        if ch == formatted_answers[index_counter1][1][index_counter2]:
            score += CORRECT
            index_counter2 += 1

        else:
            score += INCORRECT
            index_counter2 += 1

    return score, index_counter2


def format_list_answers(test_answers, formatted_answers):
    #Formats the answers by removing the newline and splitting
    #the list at the colon and every comma
    counter = 0

    while counter < len(test_answers):
        test_answers[counter] = test_answers[counter].rstrip('\n')
        test_answers[counter] = test_answers[counter].split(':')
        counter += 1

    formatted_answers = test_answers
    counter2 = 0

    while counter2 < len(formatted_answers):
        formatted_answers[counter2][1] = formatted_answers[counter2][1].split(
            ',')
        counter2 += 1

    return test_answers, formatted_answers


def main():
    #opens and reads the file, assignes contents to test answers
    score = 0.0
    grade = ''

    infile = open(TEST_ANSWERS, 'r')
    test_answers = infile.readlines()

    infile.close()

    #Creation of formatted answers
    formatted_answers = []

    format_list_answers(test_answers, formatted_answers)

    formatted_answers = test_answers

    #Creation of the answer key seperated from all answers
    answer_key = formatted_answers[0][1]

    infile = open(GRADED_TESTS, 'w')

    print('ID.   Score Grade')
    print('=================')

    header = ['ID.   Score Grade\n', '=================\n']
    infile.writelines(header)

    counter = 0
    id_counter = 1

    index_counter1 = 1
    index_counter2 = 0
    
    #loops over every item in the list of formatted answers
    #and changes the index of list.
    while counter < len(formatted_answers):
        for ch in range(len(formatted_answers)):
            score, index_counter2 = calculate_score(
                score, formatted_answers, answer_key, index_counter1, index_counter2)
            if index_counter1 < len(formatted_answers)-1:
                index_counter1 += 1
            index_counter2 = 0
            grade = letter_grade(score)

            #Prints and writes the IDs to the file
            if id_counter < len(formatted_answers):
                print(formatted_answers[id_counter][0], '', score, '', grade)
                inside = [formatted_answers[id_counter][0],
                          '  ', str(score), ' \t', grade, '\n']
                infile.writelines(inside)
                score = 0
                id_counter += 1
            counter += 1

    print('\nThe Grades are written to the file!')


if __name__ == '__main__':
    main()
