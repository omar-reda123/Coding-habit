import numpy as np

def Mean_Squared_Error(y_pred,y_true):
    pred=np.asarray(y_pred)
    gt=np.asarray(y_true)

    if pred.shape != gt.shape:
        print("Error: Arrays must have the same shape.")
        return None
    error=pred-gt
    MSE=np.mean(error**2)
    return MSE
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

print("MSE:", Mean_Squared_Error(y_pred, y_true))
# النتيجة المتوقعة: 0.375
