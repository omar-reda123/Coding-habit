import numpy as np

def train_test_split_scratch(X,y,test_size=0.2):
    if(X.shape[0]!=y.shape[0]):
        print("error, the number of samples in features does not equal number of samples in target!")
        return
    n_samples=X.shape[0]

    #indices
    indices=np.arange(n_samples)
    print(indices)

    #shuffle
    shuffled_indices=np.random.permutation(indices)
    print(shuffled_indices)

    #split
    start_train_split_idx=int(n_samples * (1 - test_size))
    train_indices=shuffled_indices[:start_train_split_idx]
    test_indices=shuffled_indices[start_train_split_idx:]

    #returning
    X_train=X[train_indices]
    X_test=X[test_indices]
    y_train=y[train_indices]
    y_test=y[test_indices]
    return X_train, X_test, y_train, y_test










#test
if __name__ == "__main__":
    X_dummy = np.array([
        [0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
        [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]
    ])
    y_dummy = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])

    print("--- Original Data ---")
    print("X shape:", X_dummy.shape, "| y shape:", y_dummy.shape)
    print("-" * 30)

    
    X_train, X_test, y_train, y_test = train_test_split_scratch(X_dummy, y_dummy, test_size=0.2)

    print("--- After Split (test_size=0.2) ---")
    print(f"X_train (80%) Shape: {X_train.shape}\n{X_train}")
    print(f"y_train (80%) Shape: {y_train.shape}\n{y_train}")
    print("-" * 30)
    print(f"X_test (20%) Shape: {X_test.shape}\n{X_test}")
    print(f"y_test (20%) Shape: {y_test.shape}\n{y_test}")


    


