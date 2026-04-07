import streamlit as st
import random

def main():
    st.title("🚗 متوقع أسعار السيارات")
    
    brand=st.selectbox("اختار الماركة:", ['Toyota', 'BMW', 'Fiat'])
    
    year=st.slider("سنة الصنع:", min_value=2000, max_value=2026, value=2015)
    
    if st.button("توقع السعر 🪄"):
        dummy_price = random.randint(150, 900)
        st.success(f"السعر المتوقع للعربية {brand} موديل {year} هو: {dummy_price} ألف! 🎉")
        
    

if __name__ == "__main__":
    main()