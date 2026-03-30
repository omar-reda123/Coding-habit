import numpy as np

def select_top_features(X, y, top_n):
    num_features = X.shape[1]
    correlations = []
    #calculating correlations
    for i in range(num_features):
        column = X[:, i]
        #mean
        X_mean=np.mean(column)
        y_mean=np.mean(y)
        #std lists
        diff_x_list=column-X_mean
        diff_y_list=y-y_mean
        #variance lists
        var_x_list=diff_x_list**2
        var_y_list=diff_y_list**2

        #correlation equation
        numerator=np.sum(diff_x_list*diff_y_list)
        denominator=np.sqrt(np.sum(var_x_list)*np.sum(var_y_list))
        r_i=numerator/denominator

        #appending to correlation list
        correlations.append((np.abs(r_i),i))

    #sorting 
    correlations.sort(reverse=True)
    
    #top indices
    top_indices = [item[1] for item in correlations[:top_n]]
    
    #new features
    X_new = X[:, top_indices]  

    #return  
    return X_new, top_indices

#test
if __name__ == "__main__":
    print("Feature Selection (Filter Method)")
    X_dummy = np.array([
        [15, 1, 100],
        [89, 2, 90],
        [42, 3, 80],
        [7,  4, 70],
        [63, 5, 60]
    ])
    y_dummy = np.array([10, 20, 30, 40, 50])

    
    X_filtered, best_cols = select_top_features(X_dummy, y_dummy, top_n=2)
    
    print(f"Best Columns Indices: {best_cols}")
    print(f"Filtered Data:\n{X_filtered}")