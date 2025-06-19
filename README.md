
# Proyecto Final de Máster - EquiTech

🎯 **Objetivo**

Este proyecto analiza la **brecha de género en el sector tecnológico español** utilizando datos oficiales del INE. Además, propone una solución práctica en forma de **aplicación web interactiva** que permite predecir, visualizar e interpretar la presencia femenina en puestos tecnológicos mediante modelos de **Machine Learning**.

---

📁 **Estructura del Proyecto**

```
Wproject_v2/
│
├── data/
│   └── datos_modelo_genero.csv           # Dataset real INE (preparado para ML)
│   └── datos_tecnologicos_genero.csv     # Dataset primer proyecto
├── src/
│   ├── modelo_genero.py                  # Entrenamiento del modelo
│   ├── modelo_entrenado.pkl              # Modelo RandomForest entrenado
│   └── encoder_genero.pkl                # Codificador OneHotEncoder
│
├── dashboards/
│   └── app.py                            # Aplicación interactiva con Streamlit
│
├── requirements.txt                      # Librerías necesarias
└── README.md                             # Este archivo
```

---

🧠 **Tecnologías utilizadas**

- Python 3.10+
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

📊 **Modelo de Machine Learning**

Se entrena un **Random Forest Classifier** con los siguientes atributos:

- `edad`: edad simulada entre 25–55 años
- `sector`: Ciencia / Tecnología / Ingeniería
- `educacion`: Primaria, Secundaria, Grado, Máster, Doctorado
- `genero_bin`: 0 = hombre, 1 = mujer

---

🧪 **Ejecución local**

1. Instala dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:

```bash
streamlit run dashboards/app.py
```

---

🔍 **Origen de los datos**

Los datos se han obtenido y procesado a partir de fuentes oficiales del [Instituto Nacional de Estadística (INE)](https://www.ine.es/) sobre ocupación por sexo, categoría y año.

Se han filtrado ocupaciones STEM (informática, ingeniería, TIC, etc.) y convertido en dataset compatible para entrenamiento.

---

📈 **Funcionalidades del dashboard**

- Interfaz Streamlit personalizable
- Predicción de probabilidad de ser mujer en un puesto STEM según:
  - Edad
  - Nivel educativo
  - Sector profesional
- Visualización de los datos introducidos
- Exportación del modelo con Joblib

---

👩‍💻 **Autoría**

Cristina Álvarez • [GitHub: LittleCriis](https://github.com/LittleCriis)

Este proyecto se enmarca como **entregable final del Máster en Data Science & IA**.

