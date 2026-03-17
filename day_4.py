def is_isogram(string):
    lower_string=string.lower()
    set_string=set(lower_string)
    return len(lower_string)==len(set_string)
       
   

   
    

# ==========================================
# Test Cases 
# ==========================================
print(is_isogram("Dermatoglyphics")) # Expected: True
print(is_isogram("isogram"))         # Expected: True
print(is_isogram("aba"))             # Expected: False
print(is_isogram("moOse"))           # Expected: False
print(is_isogram(""))                # Expected: True 