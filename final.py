#  this is out main file where we use model and train and test 



import pandas as pd
import os
import joblib
import numpy as np

from sklearn.compose import  ColumnTransformer
from sklearn.preprocessing import  OneHotEncoder,StandardScaler
from sklearn.impute import  SimpleImputer
from sklearn.model_selection import  StratifiedShuffleSplit
from sklearn.pipeline import  Pipeline
from sklearn.model_selection import cross_val_score

# Different algorithm  to train the model
# 1--> Linear Regression   2---> DescionTreeRegressor     3---.RandomForestRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error




MODEL_FILE = "model.pkl"
PIPLINE  =" pipline.pkl"

# we bild build pipline for flexiblity to conevert input data as training data
def build_pipline(num_attribytes,cat_attributes):
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
    ("num",numpipe,num_attribytes),
    ("cat",catpipe,cat_attributes)
    ])
    return fullpipeline


if not os.path.exists(MODEL_FILE):
    # train the model 
    print("Training is start ........")
    df= pd.read_csv("housing.csv")
    df["income_cat"]=pd.cut(
    df["median_income"],
    bins=[0,1.5,3.0,4.5,6.,np.inf],
    labels=[1,2,3,4,5]
   )

# create a object of StratifiedShuffleSplit
    split= StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
    for train_index,test_index in split.split(df,df["income_cat"]):
       train_set=df.iloc[train_index].drop("income_cat",axis=1)
       test_set=df.iloc[test_index].drop("income_cat",axis=1)

    housing= train_set.copy()  
    # seprate featues and label data   
    housing_labels= housing["median_house_value"].copy()
    housing_features= housing.drop("median_house_value",axis=1)


    housing_num=housing_features.drop("ocean_proximity",axis=1).columns.tolist()
    housing_cat= ["ocean_proximity"] 
    print(housing_cat)
    print(housing_num)
    pipeline = build_pipline(housing_num,housing_cat)
    housing_prepared= pipeline.fit_transform(housing_features)
    print(housing_prepared.shape)
    model = RandomForestRegressor(n_estimators=200 ,n_jobs=1, random_state=42)
    model.fit(housing_prepared,housing_labels.values.ravel())

    # save model and pipeline 
    joblib.dump(model,MODEL_FILE)
    joblib.dump(pipeline,PIPLINE)

    print("\ncongratulation your model has been trained \n Now , You can Predict your housing value\n")

else:
    print("hello i am trained \n and waiting for you data ")


    model= joblib.load(MODEL_FILE)
    pipeline= joblib.load(PIPLINE)
    # input = pd.read_csv("input.csv")
    import pandas as pd

# Create dataframe
    data = {
    "longitude": [-122.23, -118.25, -121.89, -117.16, -119.70],
    "latitude": [37.88, 34.05, 37.33, 32.72, 36.77],
    "housing_median_age": [41, 35, 20, 15, 30],
    "total_rooms": [880, 1500, 2500, 1800, 2100],
    "total_bedrooms": [129, 300, 450, 350, 400],
    "population": [322, 800, 1200, 950, 1100],
    "households": [126, 280, 400, 320, 380],
    "median_income": [8.3252, 4.5000, 6.2000, 3.7500, 5.1000],
    "ocean_proximity": ["NEAR BAY", "INLAND", "NEAR OCEAN", "<1H OCEAN", "INLAND"]
}

    df = pd.DataFrame(data)


# doubt here how pipline transform input data 
    transformed_input = pipeline.transform(df)
    prediction = model.predict(transformed_input)
    df["median_house_value"]=prediction
    df.to_csv("output2.csv")
    print(pipeline)