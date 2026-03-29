from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score
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
#modeling
param_distributions = {
    'n_estimators': [50, 100, 200],      #Number of trees
    'max_depth': [10, 15, 20, None],     #Maximum Depth
    'min_samples_split': [2, 5, 10]      #Minimum number of houses to create a new tree branch
}
Rf=RandomForestRegressor(random_state=42)

search_hyperparameters_model=RandomizedSearchCV(
    estimator=Rf,
    param_distributions=param_distributions,
    n_iter=10,
    cv=3,
    random_state=42,
    n_jobs=-1
)

#training
search_hyperparameters_model.fit(X_train,y_train)
#voting
best_model=search_hyperparameters_model.best_estimator_
#evalution
best_rf_predictions=best_model.predict(X_train)
mse=mean_squared_error(y_pred=best_rf_predictions,y_true=y_train)
r_2=r2_score(y_pred=best_rf_predictions,y_true=y_train)
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r_2}")




"""
conclusions:
on train:
Mean Squared Error: 0.0492361568031483
R-squared Score: 0.9631680436074431

on test:
Mean Squared Error: 0.25616067857780245
R-squared Score: 0.804518526024086

overfitting is reduced a little bit


"""

