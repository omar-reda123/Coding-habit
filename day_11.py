from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#loading data
print("Loading data...")
housing = fetch_california_housing()
X = housing.data    #features
y = housing.target  #target 

print(f"Dataset size: {X.shape[0]} houses")


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)

LR = LinearRegression()
LR.fit(X_train,y_train)


predictions = LR.predict(X_test)

mse = mean_squared_error(y_pred=predictions,y_true=y_test)
r2 = r2_score(y_pred=predictions,y_true=y_test)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

"""
results:
Mean Squared Error: 0.5558915986952425
R-squared Score: 0.5757877060324521

Conclusion:
There is an underfitting here, the model is simpler than the data
"""