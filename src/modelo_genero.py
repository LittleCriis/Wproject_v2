import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report
import joblib
import numpy as np

# Cargar datos
df = pd.read_csv('data/datos_genero.csv')
df = df.dropna()
X = df[['edad', 'sector', 'educacion']]
y = df['genero_bin']

# Codificar
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_cat = encoder.fit_transform(X[['sector', 'educacion']])
X_num = X[['edad']].values
X_proc = np.hstack([X_num, X_cat])

# Guardar encoder
joblib.dump(encoder, 'src/encoder_genero.pkl')

# Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X_proc, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, 'src/modelo_entrenado.pkl')

# Reporte
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
