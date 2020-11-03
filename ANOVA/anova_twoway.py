import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

music = np.repeat(['Constant Sound', 'No Sound'], 15)
age = np.tile(np.repeat(['4-8', '8-13', '13-17'], 5), 2)
score = [6 ,5, 5, 2, 4, 4, 5, 6, 9, 8,
7, 6, 10, 8, 9, 1, 3, 2, 1, 2, 4, 5, 6, 7, 3, 6, 6, 4, 7, 5]

# Create data frame
df = pd.DataFrame({'Music' : music, 'Age' : age, 'Score' : score})
print(df)

# Perform two-way ANOVA
model = ols('Score ~ C(Music) + C(Age) + C(Music):C(Age)', data=df).fit()
sm.stats.anova_lm(model, typ=2)
