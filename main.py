# this  is the mini  project  by python California House Preiction 
# 
import pandas as pd

import numpy as np

from sklearn.compose import  ColumnTransformer
from sklearn.preprocessing import  OneHotEncoder,StandardScaler
from sklearn.impute import  SimpleImputer
from sklearn.model_selection import  StratifiedShuffleSplit
from sklearn.pipeline import  Pipeline
from sklearn.model_selection import cross_val_score
# Different algorithm  to train the model
# 1--> Linear Regression   2---> DescionTreeRegressor     3---.RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error


# 1.  Load the CSV file
df= pd.read_csv("housing.csv")

# 2 -->split train and test data from the main data by using StratifiedSuffle Split on income_cat
df["income_cat"]=pd.cut(
    df["median_income"],
    bins=[0,1.5,3.0,4.5,6.,np.inf],
    labels=[1,2,3,4,5]
)

# create a object of StratifiedShuffleSplit
split= StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(df,df["income_cat"]):
    train_set=df.iloc[train_index].drop("income_cat",axis=1)
    # test_set=df.iloc[test_index].drop("income_cat",axis=1)

# we work on 
housing= train_set.copy()   

# Seprate labels and feature 
housing_labels= housing[["median_house_value"]].copy()
housing= housing.drop("median_house_value",axis=1)


# seprate Categorical data and numeriacal data
housing_num=housing.drop("ocean_proximity",axis=1).columns.tolist()
housing_cat= ["ocean_proximity"]
# print(housing_cat)

# pipeline
# 1 numerical pipeline
numpipe= Pipeline([
    ("imputer",SimpleImputer(strategy="median")),
    ("scale",StandardScaler())
]
)

# 2--> Categorical pipeline
catpipe= Pipeline([
    ("hotencoder",OneHotEncoder(handle_unknown="ignore"))
])

#  Craete a full pipline 
fullpipeline= ColumnTransformer([
    ("num",numpipe,housing_num),
    ("cat",catpipe,housing_cat)
])

# apply fit and transform on full pipeline 
housing_prepared= fullpipeline.fit_transform(housing)
print(housing_prepared.shape)
# print(housing_prepared.head())
# housing_prepared_df=pd.DataFrame(housing_prepared,columns=housing.columns,index=housing.index)
# print(housing_prepared_df)



#  Train the Model 

# 1 Linear Regression 
# linreg= LinearRegression()
# linreg.fit(housing_prepared,housing_labels)
# lin_pred=linreg.predict(housing_prepared)
# # lin_rmse= root_mean_squared_error(housing_labels,lin_pred)
# # cross validation is use to test error without test_set 
# lin_cv= -cross_val_score( linreg,housing_prepared,housing_labels,scoring="neg_root_mean_squared_error",cv=10

# )
# # print(f"the root mean square error for liner regreesion  {lin_cv}")
# print(pd.Series(lin_cv).describe())




# # 2- Decision tree 
# decreg= DecisionTreeRegressor()
# decreg.fit(housing_prepared,housing_labels)
# dec_pred=decreg.predict(housing_prepared)
# # dec_rmse= root_mean_squared_error(housing_labels,dec_pred)
# dec_cv= -cross_val_score( decreg,housing_prepared,housing_labels,scoring="neg_root_mean_squared_error",cv=10

# )
# print(pd.Series(dec_cv).describe())


# 3--  Random Forest Regresssor
ranreg= RandomForestRegressor()
ranreg.fit(housing_prepared,housing_labels.values.ravel())
ran_pred=ranreg.predict(housing_prepared)
# ran_rmse= root_mean_squared_error(housing_labels,ran_pred)
ran_cv= -cross_val_score( ranreg,housing_prepared,housing_labels.values.ravel(),scoring="neg_root_mean_squared_error",cv=10

)
print(pd.Series(ran_cv).describe())
# print(f"the root mean square error for Random regreesion  {ran_rmse}")
#  Conclusion  --->
    # Random Forest Classifier give less error with respect to decsion and Linear Regression

