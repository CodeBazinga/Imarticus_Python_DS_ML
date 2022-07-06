from sklearn import datasets

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

iris=datasets.load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y)
log_reg = LogisticRegression(max_iter=1000)
svc_model = SVC()
dt_model = DecisionTreeClassifier()
rf_model = RandomForestClassifier()
log_reg = log_reg.fit(x_train,y_train)
svc_model = svc_model.fit(x_train,y_train)
dt_model = dt_model.fit(x_train,y_train)
rf_model = rf_model.fit(x_train,y_train)


pickle.dump(log_reg,open('log_model.pkl','wb'))
pickle.dump(svc_model,open('svc_model.pkl','wb'))
pickle.dump(log_reg,open('dt_model.pkl','wb'))
pickle.dump(svc_model,open('rf_model.pkl','wb'))

