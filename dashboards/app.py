import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("Predicción de presencia femenina en tecnología")

# Cargar modelo y encoder
encoder = joblib.load('src/encoder_genero.pkl')
modelo = joblib.load('src/modelo_entrenado.pkl')

# Inputs del usuario
edad = st.slider("Edad", 18, 65, 30)
sector = st.selectbox("Sector", ["Software", "Hardware", "Consultoría", "Otros"])
educacion = st.selectbox("Nivel educativo", ["Primaria", "Secundaria", "Grado", "Máster", "Doctorado"])

# Procesamiento
input_df = pd.DataFrame({"edad": [edad], "sector": [sector], "educacion": [educacion]})
X_num = input_df[['edad']].values
X_cat = encoder.transform(input_df[['sector', 'educacion']])
X_proc = np.hstack([X_num, X_cat])

# Mostrar entrada
st.write("Datos introducidos:", input_df)

# Predicción
prob = modelo.predict_proba(X_proc)[0][1]
st.write(f"🔹 Probabilidad de que sea mujer en puesto tecnológico: **{prob:.2%}**")


