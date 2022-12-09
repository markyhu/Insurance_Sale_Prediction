import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load data
dataset1=pd.read_excel('./MockDataSet1.xlsx',index_col=0)
missing =['{ND}','X','XX',-999997]

#rename columns for easier access
rename_cols = {'Joint?':'Joint','Person1 Age':'Age','JF (Score)':'Score',
                'WGB (No. of other addresses held)':'Other_addresses',
                'X (Months same person on ER at current address)':'Months_ER',
                'EF (No. of people not same surname at current address)':'Other_people',
                'BB (Number of CCJs)': 'CCJs','ND (Months since last CCJ)': 'Months_after_CCJ',
                'NOB (Property group)': 'Property_group','URB (Income group)':'Income_group',
                'LSB (Regional banded house price band)': 'House_price_band',
                }
dataset1.rename(columns=rename_cols,inplace=True)

#drop duplicates and clean special values
dataset1.drop_duplicates(inplace=True)
dataset1.dropna(subset=['Smoker'],inplace=True) 
dataset1['Score'].replace(9999,np.nan,inplace=True)
dataset1['House_price_band'].replace(99,np.nan,inplace=True)
dataset1.replace(missing,np.nan,inplace=True)

#encode categorical variables
obj_cols = dataset1.select_dtypes(include='object').columns
dataset1[obj_cols] = dataset1[obj_cols].astype('string')

dataset1['Sale'] = [1 if i == 'Y' else 0 for i in dataset1['Sale']]
dataset1['Smoker']=[1 if i =='Y' else 0 for i in dataset1['Smoker']]
dataset1['Joint']=[1 if i =='Y' or i=='Yes' else 0 for i in dataset1['Joint']]
dataset1['Channel']=dataset1['Channel'].map({'CTM':0,'Direct':1,'MSM':2})
dataset1['Product']=dataset1['Product'].map({'Level':0, 'Level accelerated':1,'Level with CI':2,
                                        'Decreasing':3,'Decreasing with CI':4,'Decreasing accelerated':5})

num_cols=['Age','Term', 'TotalPremium', 'GrossCommission', 'Score','Months_ER',
       'Other_addresses', 'Other_people', 'CCJs','Months_after_CCJ']
cat_cols= ['Channel', 'Smoker', 'Joint','Product']  
ord_cols=['Income_group', 'House_price_band','Property_group']


#plotting
sns.displot(data=dataset1, x='House_price_band', stat='percent', col='Sale', height=4,common_norm=False,discrete=True)
plt.show()

sns.catplot(data=dataset1,  x="Sale",y="Other_addresses", kind="box")
plt.show()


######## Modeling ########


from numpy import sort
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.feature_selection import SelectFromModel



X =dataset1[num_cols+cat_cols+ord_cols].drop('Months_after_CCJ',axis=1)
target = dataset1.Sale

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.3, random_state=7)

# fit model on all training data
model = XGBClassifier(importance_type='gain')
model.fit(X_train, y_train)

plt.rcParams["figure.figsize"] = (14, 7)
plot_importance(model,importance_type='gain',show_values=False)
plt.show()
# plt.savefig('./image/feature_importance.png')

# make predictions for test data and evaluate
y_pred = model.predict(X_test)
F1 = f1_score(y_test, y_pred)
print("F1: %.2f%%" % (F1 * 100.0))

# Fit model using each importance as a threshold
thresholds = sort(model.feature_importances_)
for thresh in thresholds:
    # select features using threshold
    selection = SelectFromModel(model, threshold=thresh, prefit=True)
    select_X_train = selection.transform(X_train)
    
    # train model
    selection_model = XGBClassifier()
    selection_model.fit(select_X_train, y_train)
    
    # eval model
    select_X_test = selection.transform(X_test)
    y_pred = selection_model.predict(select_X_test)
    F1=f1_score(y_test, y_pred)
    print("Thresh=%.3f, n=%d, F1_Score: %.2f%%" % (thresh, select_X_train.shape[1], F1*100.0))


