from scipy.stats import f_oneway as owanova
import pandas as pd

'''
A firm wishes to compare four programs for training workers to perform a certain manual task. Twenty new employees are randomly assignment to the training programs, with 5 in each program. At the end of the training period, a test is conducted to see how quickly trainees can perform the task. the number of times the task is performed per minute is recorded for each trainee.
'''

Pr1 = [9, 12, 14, 11, 13]
Pr2 = [10, 6, 9, 9, 10]
Pr3 = [12, 14, 11, 13, 11]
Pr4 = [9 , 8, 11, 7, 8]

d = {'Pr1': Pr1, 'Pr2': Pr2, 'Pr3': Pr3, 'Pr4': Pr4}
df = pd.DataFrame(data = d)
boxplot = df.boxplot(column = ['Pr1', 'Pr2', 'Pr3', 'Pr4'])

owanova(Pr1, Pr2, Pr3, Pr4)
