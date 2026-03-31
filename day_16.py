import numpy as np

def standardize_data(X):
    means=np.mean(X,axis=0)
    stds=np.std(X,axis=0)
    X_scaled = (X-means)/stds
    return X_scaled
    

#test
if __name__ == "__main__":
    print("Data Standardization")
    X_dummy = np.array([
    [1.6, 50000, 2010],
    [2.0, 120000, 2015],
    [1.4, 30000, 2008],
    [3.5, 200000, 2020],
    [1.8, 80000, 2012]
    ])
    
    X_scaled = standardize_data(X_dummy)
    
    print("Original Data:\n", X_dummy)
    print("\nScaled Data:\n", np.round(X_scaled, 2))
