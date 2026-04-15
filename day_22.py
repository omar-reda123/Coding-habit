import numpy as np

class BaseEncoder:
    def __init__(self):
        self.is_fitted = False

    def fit_transform(self, column):
        self.fit(column)
        return self.transform(column)

class CustomOrdinalEncoder(BaseEncoder): 
    
    def __init__(self, mapping_dict):
        super().__init__() 
        self.mapping_dict = mapping_dict

    def fit(self, column):
        self.is_fitted = True

    def transform(self, column):
        if not self.is_fitted:
            print("Error: You must fit the encoder first!")
            return None
            
        return np.array([self.mapping_dict[category] for category in column])

# --- منطقة الاختبار ---
if __name__ == "__main__":
    conditions = np.array(['Good', 'Bad', 'Excellent', 'Good'])
    condition_map = {'Bad': 0, 'Good': 1, 'Excellent': 2}
    ordinal_enc = CustomOrdinalEncoder(condition_map)
    encoded_data = ordinal_enc.fit_transform(conditions)
    print("Is it fitted?", ordinal_enc.is_fitted) 
    print("Encoded Data:\n", encoded_data)