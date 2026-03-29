#Keeping up with modeling concepts in ML
#K-fold Cross-validation (data partitioning strategy => more generalized model)
#It may used to: 1)evaluating a model’s performance 2)hyperparameter tuning

#library
import  numpy as np

#function
def k_fold_cv_indices(n_samples,k=5):
    indices=np.arange(n_samples)
    np.random.shuffle(indices)
    fold_size=int(n_samples/k)
    folds=[]
    for i in range(k):
        start_idx=i*fold_size
        end_idx=start_idx+fold_size
        test_indices=indices[start_idx:end_idx]
        train_indices=np.concatenate((indices[:start_idx],indices[end_idx:]))
        folds.append((train_indices,test_indices))
    
    return folds


#test
result = k_fold_cv_indices(21, 5)

for i, (train, test) in enumerate(result):
    print(f"Fold {i+1}:")
    print(f"  Train (Yellow) -> {train}")
    print(f"  Test  (Blue)   -> {test}\n")




    


