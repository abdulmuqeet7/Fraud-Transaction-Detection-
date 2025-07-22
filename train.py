import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score,roc_auc_score,make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import NearMiss #For undersampling the data
import joblib
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

from sklearn.metrics import accuracy_score
df = pd.read_csv('data/Bank_Transaction_Fraud_Detection.csv')
df.drop(['Customer_Email','Customer_Contact','Transaction_Currency','Customer_Name','Customer_ID','Transaction_ID','Merchant_ID'],axis=1,inplace=True)

#Label encoding the columns
label_encoder = LabelEncoder()
df['Account_Type']=label_encoder.fit_transform(df['Account_Type'])
df['Gender']=label_encoder.fit_transform(df['Gender'])
df['Transaction_Type']=label_encoder.fit_transform(df['Transaction_Type'])
df['Merchant_Category']=label_encoder.fit_transform(df['Merchant_Category'])
df['Device_Type']=label_encoder.fit_transform(df['Device_Type'])
joblib.dump(label_encoder,"label_encoder.pkl")

#Getting Dependent and Independent features
X = df.drop(['Is_Fraud'],axis=1)
Y = df['Is_Fraud']

#One-hot encoding
City = pd.get_dummies(X['City'],drop_first=True,dtype=int) #To prevent the dummy variable trap
Gender = pd.get_dummies(X['Gender'],drop_first=True,dtype=int)
X.drop(['Gender','City'],axis=1,inplace=True)
State = pd.get_dummies(X['State'],drop_first=True,dtype=int)
Bank_Branch = pd.get_dummies(X['Bank_Branch'],drop_first=True,dtype=int)
Transaction_Device=pd.get_dummies(X['Transaction_Device'],drop_first=True,dtype=int)
Transaction_Location = pd.get_dummies(X['Transaction_Location'],drop_first=True,dtype=int)
Transaction_Description = pd.get_dummies(X['Transaction_Description'],drop_first=True,dtype=int)
X.drop(['State','Bank_Branch','Transaction_Device','Transaction_Location','Transaction_Description'],axis=1,inplace=True)
X=pd.concat([X,State,Bank_Branch,Transaction_Device,Transaction_Location,Transaction_Description,City,Gender],axis=1)
X.columns = X.columns.astype(str) #Converting Columns to strings

#Splitting the date time columns
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], format='%d-%m-%Y', errors='coerce')
dates= df['Transaction_Date']

# Extract the day and store it in a new series
transaction_day = dates.dt.day
transaction_month = dates.dt.month
transaction_year = dates.dt.year
X = pd.concat([X,transaction_day,transaction_month,transaction_year],axis=1)
X.drop(['Transaction_Date'],axis=1,inplace=True)
X = pd.concat([X,transaction_day.rename('transaction_day'),transaction_month.rename('transaction_month'),transaction_year.rename('transaction_year')],axis=1)

#Doing same for time
times = pd.to_datetime(df['Transaction_Time'], format='%H:%M:%S', errors='coerce')
transaction_hour = times.dt.hour
transaction_minute = times.dt.minute
transaction_second = times.dt.second
X.drop(['Transaction_Time'],axis=1,inplace=True)
X = pd.concat([X,transaction_hour.rename('transaction_hour'),transaction_minute.rename('transaction_minute'),transaction_second.rename('transaction_second')],axis=1)
X.drop(['Chandigarh','Puducherry'],axis=1,inplace=True) #dropping the duplicate columns, due to one-hot encoding

#Splitting into train test and split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

#Undersampling the data
from imblearn.under_sampling import NearMiss
ns = NearMiss(sampling_strategy=0.7)
X_train_ns,y_train_ns=ns.fit_resample(X_train,y_train)

#Creating XGBoost model
model = xgb.XGBClassifier(reg_lambda=20,min_child_weight=4,max_depth=15,learning_rate=np.float64(0.05),colsample_bytree=0.5,gamma=0.2,objective='binary:logistic',n_jobs=-1,booster='gbtree',scale_pos_weight=1,eval_metric='aucpr')
#I have already performed hyperparameter tuning in jupyter notebook
model.fit(X_train_ns,y_train_ns)

#Predict
y_proba = model.predict_proba(X_test)
y_pred = (y_proba[:, 1] >= 0.45).astype(int)

#model evaluation
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#save trained model
joblib.dump(model, "model/model.pkl")