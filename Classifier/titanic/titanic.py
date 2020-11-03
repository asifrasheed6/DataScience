import pandas as pd

training_sample_size = 700
training_data = pd.read_csv('train.csv', usecols = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']).sample(n = training_sample_size) # Generates random sample of training_sample_size entries without replacement from the train data set (replace = False by default)

p_survived = training_data.groupby('Survived').size() / training_sample_size # Probability of Survival and Death

p_class_survived = training_data.groupby(['Pclass', 'Survived']).size() / training_sample_size / p_survived # Probability of Survival or Death for Every Ticket Class
p_sex_survived = training_data.groupby(['Sex', 'Survived']).size() / training_sample_size / p_survived # Probability of Survival or Death for Every Sex
p_age_survived = training_data.groupby(['Age', 'Survived']).size() / training_sample_size / p_survived # Probability of Survival or Death for Every Age
p_sibsp_survived = training_data.groupby(['SibSp', 'Survived']).size() / training_sample_size / p_survived # Probability of Survival or Death for each number of Siblings or Spouses
p_parch_survived = training_data.groupby(['Parch', 'Survived']).size() / training_sample_size / p_survived # Probability of Survival or Death for each number of Parent or Children

def didSurvive(row):
    try:
        p_survived_yes = p_class_survived[row['Pclass']][1] * p_sex_survived[row['Sex']][1] * p_age_survived[row['Age']][1] * p_sibsp_survived[row['SibSp']][1] * p_parch_survived[row['Parch']][1]
        p_survived_no = p_class_survived[row['Pclass']][0] * p_sex_survived[row['Sex']][0] * p_age_survived[row['Age']][0] * p_sibsp_survived[row['SibSp']][0] * p_parch_survived[row['Parch']][0]
        return 1 if p_survived_yes > p_survived_no else 0
    except KeyError: # If any passenger information is missing or wasn't part of the training data
        return 0

sample_size = 100
data = pd.read_csv('test.csv', usecols = ['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']).sample(n = sample_size) # Generates random sample of sample_size entries without replacement from the test set (replace = False by default)
data['Survived'] = 0

for index, row in data.iterrows():
    data.at[index, 'Survived'] = didSurvive(row)
        
pd.to_numeric(data.Survived, downcast='integer')

data[['PassengerId', 'Survived']].to_csv('result.csv', index=False)
