from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

#loading data
print("Loading data...")
housing = fetch_california_housing()
X = housing.data    #features
y = housing.target  #target 

print(f"Dataset size: {X.shape[0]} houses")


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)

RF = RandomForestRegressor(random_state=42)
RF.fit(X_train,y_train)


RF_predictions = RF.predict(X_test)

mse = mean_squared_error(y_pred=RF_predictions,y_true=y_test)
r2 = r2_score(y_pred=RF_predictions,y_true=y_test)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

"""
For linear regression:
On train data:
Mean Squared Error: 0.5179331255246697
R-squared Score: 0.6125511913966952 
):
On test data:
Mean Squared Error: 0.5558915986952425
R-squared Score: 0.5757877060324521

That is underfitting, the accuracy is realy bad on the training,test data.
Hence, Now I will try a more complex model on this dataset.

For Random Forest Regressor:
On train data:
Mean Squared Error: 0.035327529696893685
R-squared Score: 0.9735726320302575
That is predictable because it is the training data that it fitted already

):
On test data:
Mean Squared Error: 0.2553684927247781
R-squared Score: 0.8051230593157366
there is now a little bit trade-off between bias and variance, looking foroward to reduce overfitting someway.

"""

