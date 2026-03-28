from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV
#loading data
print("Loading data...")
housing = fetch_california_housing()
X = housing.data    #features
y = housing.target  #target 
print(f"Dataset size: {X.shape[0]} houses")
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)

"""
    There was a problem in the previous random forest model, causing an overfitting(97% r2 on training, 80% r2 on test)
    , Now I will try a random search Cross-Validation to try all hyperparameters(max_depth,min_samples_split,n_estimators)

"""



"""
conclusions:

"""

