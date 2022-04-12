# CTI-110 
# P2HW2 - Score Avg 
# Christian Mcfadden 
# 2-22-22
#

## declare score 1-7
score1 = float(input('Enter Score #1: '))
score2 = float(input('Enter Score #2: '))
score3 = float(input('Enter Score #3: '))
score4 = float(input('Enter Score #4: '))
score5 = float(input('Enter Score #5: '))
score6 = float(input('Enter Score #6: '))
score7 = float(input('Enter Score #7: '))

## calculations


the_list = [score1, score2, score3, score4, score5, score6, score7]
divide = len(the_list)
score_avg = (score1 + score2 + score3 + score4 + score5 + score6 + score7)/ divide
minimum = min(the_list)


## show results lowest score- modified list-scores average
print('-----------Results------------')
print('Lowest Score   : ', minimum)
print('Modified List  : ', the_list)
print('Scores Average : ', format(score_avg,'.2f'))
print('------------------------------')
