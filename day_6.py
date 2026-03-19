import numpy as np
import time

def softmax_loop(x): #non pythonic_way
    x = np.asarray(x)
    softmax_array=[]
    for i in range(len(x)):
        softmax_element=(np.exp(x[i])/np.sum(np.exp(x)))
        softmax_array.append(softmax_element)
    return softmax_array

def softmax_vectorized(x): #pythonic_way
    x = np.asarray(x) 
    exps=np.exp(x) #numpy array of e^x_i
    return exps/np.sum(exps) #numpy array of softmax(x)


# ==========================================
# Test Cases 
# ==========================================
big_array = np.random.rand(10000)

print("Testing execution time...\n")

#time for looping
start_time_loop = time.time()     
softmax_loop(big_array)             
end_time_loop = time.time()       
loop_duration = end_time_loop - start_time_loop
print(f"Time using For Loop:     {loop_duration:.5f} seconds")

#time for vectorization
start_time_vec = time.time()     
softmax_vectorized(big_array)       
end_time_vec = time.time()        
vec_duration = end_time_vec - start_time_vec
print(f"Time using Vectorization: {vec_duration:.5f} seconds")