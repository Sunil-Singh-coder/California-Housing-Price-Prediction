Information divided into three part 
1.  Frontent Area      -----> ( start from line 25)

2.  Backend Area         -----> ( start from line 40)

3.  Data Set Inforamtion         -----> ( start from line 60)




Task 1:
   Our Goal is develop this model with frontent so that use can easily see rent for home 












<---------------------------Frontent Area----------------------------------->
(Note:-> This Part will filled by frontent by developer )

Frontend developers should create input fields for all dataset features: longitude, latitude, 
housing_median_age, total_rooms, total_bedrooms, population, households, median_income, 
and ocean_proximity. These inputs are sent to the trained model, which returns
the predicted median_house_value (house price).








<-------------------------------- Backend Area------------------------------->
housing.csv  ---> 
   in housing.csv we have data for train the model 


input.csv --->
   i made this csv file for testing purpose

main.py---> 
   main.py is our main file from where we will execute out model 

model.pkl---->
  In this we contain our trained model,so we can use any where any time without train again







#####------------------------------------ Dataset Information----------------------------------------->

This project uses the California Housing dataset to train the machine learning model for house price prediction.

### Features Used

| Column Name        | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| longitude          | Longitude of the house location                            |
| latitude           | Latitude of the house location                             |
| housing_median_age | Median age of houses in the area                           |
| total_rooms        | Total number of rooms                                      |
| total_bedrooms     | Total number of bedrooms                                   |
| population         | Population of the area                                     |
| households         | Number of households in the area                           |
| median_income      | Median income of residents in the area                     |
| ocean_proximity    | Distance of the house from the ocean (categorical feature) |

### Target Variable

| Column Name        | Description                                    |
| ------------------ | ---------------------------------------------- |
| median_house_value | House price/value to be predicted by the model |


### Model Input

The frontend should collect the following user inputs:
* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

These values are passed to the trained model, which predicts the estimated house value.

