import numpy as np

def sigmoid(x):
    x = np.asarray(x)
    return 1/(1+np.exp(-x))
    

def relu(x):
    x = np.asarray(x)
    return np.maximum(0,x)
    

# ==========================================
# Test Cases 
# ==========================================
test_array = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

print("Original Array:", test_array)
print("Sigmoid Output:", sigmoid(test_array))
# النتيجة المتوقعة تقريباً: [0.1192, 0.2689, 0.5, 0.7310, 0.8807]

print("ReLU Output:   ", relu(test_array))
# النتيجة المتوقعة: [0., 0., 0., 1., 2.]