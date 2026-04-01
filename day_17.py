import numpy as np
def r2_score_scratch(y_true, y_pred):
    y_mean = np.mean(y_true)
    ss_res = np.sum((y_pred-y_true)**2)
    ss_tot = np.sum((y_true-y_mean)**2)
    r2 = 1-(ss_res/ss_tot)
    return r2
    pass

#test
if __name__ == "__main__":
    y_true = np.array([100, 150, 200, 250, 300])
    y_pred = np.array([110, 140, 210, 240, 290])
    
    score = r2_score_scratch(y_true, y_pred)
    print(f"R-Squared Score: {np.round(score, 4)}") 
