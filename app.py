import streamlit as st
import joblib
import numpy as np

st.title("Kilo Tahmini Uygulaması")
st.write("Lütfen boyunuzu giriniz:")

# kullanıcı bilgi girişi
kilo = st.number_input("Boy (cm):",min_value=0, max_value=200, value=1, step=1)

# tahmin edilecek kilo
if st.button("Hesapla"):
    # Modeli yükle
    model= joblib.load('linear_model.pkl')
  
    # tahmin 
    prediction = model.predict(np.array([[kilo]]))

    # sonucu göster
    st.success(f"Tahmini kilo: {prediction[0]:,.2f} kg ")
