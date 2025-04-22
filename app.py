import streamlit as st
import joblib
import numpy as np

# Ba�l�k    
st.title("Kilo Tahmini Uygulaması")
st.write("Lütfen boyunuzu giriniz:")

# Kullan�c�dan bilgi giri�i al
kilo = st.number_input("Boy (cm):",min_value=0, max_value=200, value=1, step=1)

# Butona bas�ld���nda tahmin edilecek
if st.button("Hesapla"):
    # Modeli y�kle
    model= joblib.load('linear_model.pkl')
  
    # Tahmin yap
    prediction = model.predict(np.array([[kilo]]))

    # Sonucu g�ster
    st.success(f"Tahmini kilo: {prediction[0]:,.2f} kg ")