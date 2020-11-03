from covid19dh import covid19
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

X, Y, Z = {}, {}, {}

data, ignore = covid19('Indonesia', start = "2020-03-19", end = "2020-09-20", verbose = False)

X['Indonesia'] = [y-x for x,y in zip(data.confirmed.to_list(), data.confirmed.to_list()[1:])] # Number of new cases per day for Indonesia
Y['Indonesia'] = [y-x for x,y in zip(data.recovered.to_list(), data.recovered.to_list()[1:])] # Number of new recoveries per day for Indonesia
Z['Indonesia'] = [y-x for x,y in zip(data.deaths.to_list(), data.deaths.to_list()[1:])] # Number of new deaths per day for Indonesia


data, ignore = covid19('Philippines', start = "2020-03-19", end = "2020-09-20", verbose = False)

X['Philippines'] = [y-x for x,y in zip(data.confirmed.to_list(), data.confirmed.to_list()[1:])] # Number of new cases per day for Philippines
Y['Philippines'] = [y-x for x,y in zip(data.recovered.to_list(), data.recovered.to_list()[1:])] # Number of new recoveries per day for Philippines
Z['Philippines'] = [y-x for x,y in zip(data.deaths.to_list(), data.deaths.to_list()[1:])] # Number of new deaths per day for Philippines


data, ignore = covid19('Germany', start = "2020-03-19", end = "2020-09-20", verbose = False)

X['Germany'] = [y-x for x,y in zip(data.confirmed.to_list(), data.confirmed.to_list()[1:])] # Number of new cases per day for Germany
Y['Germany'] = [y-x for x,y in zip(data.recovered.to_list(), data.recovered.to_list()[1:])] # Number of new recoveries per day for Germany
Z['Germany'] = [y-x for x,y in zip(data.deaths.to_list(), data.deaths.to_list()[1:])] # Number of new deaths per day for Germany

plt.style.use('seaborn-whitegrid')

plt.title('Daily New Cases for Germay')
plt.plot(pd.date_range('20-03-20', '20-09-20').tolist(), X['Germany'], 'o', color='black')
plt.show(block=True)

plt.title('Daily Recoveries for Germay')
plt.plot(pd.date_range('20-03-20', '20-09-20').tolist(), Y['Germany'], 'o', color='black')
plt.show(block=True)

plt.title('Daily Deaths for Germay')
plt.plot(pd.date_range('20-03-20', '20-09-20').tolist(), Z['Germany'], 'o', color='black')
plt.show(block=True)
