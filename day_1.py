import numpy as np


def euclidean_distance(point1, point2):
    array_1=np.asarray(point1)
    array_2=np.asarray(point2)
    if((array_1.ndim!=1)or(array_2.ndim!=1)):
        print("error!, must be one row only ")
        return None
    if array_1.shape != array_2.shape:
        print("Error! Points must have the same number of coordinates.")
        return None
    
    distance=np.sqrt(np.sum((array_1-array_2)**2))
    return distance
# ==========================================
# Test Cases (حالات الاختبار)
# ==========================================

# Test Case 1: 2D points (نقطتين في مستوى ثنائي الأبعاد)
p1 = np.array([1, 2])
p2 = np.array([4, 6])
print("Test 1 (2D):", euclidean_distance(p1, p2)) 
# النتيجة المتوقعة: 5.0

# Test Case 2: 3D points (نقطتين في مستوى ثلاثي الأبعاد)
p3 = np.array([1, 2, 3])
p4 = np.array([4, 5, 6])
print("Test 2 (3D):", euclidean_distance(p3, p4)) 
# النتيجة المتوقعة: 5.196152422706632
