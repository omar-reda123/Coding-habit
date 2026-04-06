import numpy as np

def ordinal_encode_from_scratch(column, mapping_dict):
    return np.array([mapping_dict[category] for category in column])
def one_hot_encode_scratch(column):
    unique_categories=np.unique(column)
    mapping_dict = {val: i for i, val in enumerate(unique_categories)}
    indices = np.array([mapping_dict[val] for val in column])
    identity_matrix = np.eye(len(unique_categories))
    encoded_matrix=identity_matrix[indices]
        
    return encoded_matrix, unique_categories
    

#test
if __name__ == "__main__":
    #ordinal
    conditions = np.array(['Good', 'Bad', 'Excellent', 'Good', 'Bad'])
    condition_map = {'Bad': 0, 'Good': 1, 'Excellent': 2}
    encoded_conditions = ordinal_encode_from_scratch(conditions, condition_map)
    print("Ordinal Encoded:\n", encoded_conditions)

    #nominal
    cars = np.array(['Toyota', 'BMW', 'Fiat', 'Toyota', 'Fiat'])
    encoded_data, classes = one_hot_encode_scratch(cars)
    print("Classes found:", classes)
    print("Encoded Matrix:\n", encoded_data)
