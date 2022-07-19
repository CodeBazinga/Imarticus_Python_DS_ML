from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np
import seaborn as sns
import pickle

df = pd.read_csv('iris.csv')
x = df.iloc[:, :-1] 
y = df.iloc[:, -1] 

m1 = RandomForestClassifier(n_estimators=90,criterion='gini',
                            max_depth=4,min_samples_split=15)
m1.fit(x, y) 

pickle.dump(m1, open('model.pkl','wb')) # save the model
print('Model Stored')

