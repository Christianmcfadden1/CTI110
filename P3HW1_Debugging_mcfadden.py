# this program will determine the grade you were giving
# christian Mcfadden

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    a_score = 90
    b_score = 80
    c_score = 70
    d_score = 60
    e_score = 50

    score = int(input('please enter grade: '))

    if score >= a_score:
        print('Your grade is: A')
    elif score > b_score:
        print('Your grade is: B')
    elif score >= c_score:
        print('Your grade is: C')
    elif score > d_score:
         print('Your grade is: D')
    elif score >= e_score:
        print('Your grade is: E')
    else:
        print('Your grade is: F')
    # TO DO: finish this

    # TO DO: define the rest of the scores

    







# program start
main()
