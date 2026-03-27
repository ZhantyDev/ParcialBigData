import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, mean_squared_error, r2_score

df = pd.read_csv('data\sdss_sample.csv')
df.head()

print("Valores nulos antes de la limpieza:")
print(df.isnull().sum())

class_mapping = {
    'GALAXY': 1,
    'STAR': 2,
    'QSO': 3
}
df['class'] = df['class'].str.upper().map(class_mapping)

# 1. Preparar variables según requerimientos: u, g, r, i, z, redshift
features_class = ['u', 'g', 'r', 'i', 'z', 'redshift']
X_class = df[features_class]
y_class = df['class'] # Target original

# División 70/30
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.3, random_state=42, stratify=y_class)

# Inicializar y entrenar KNN con k=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_c, y_train_c)

# Predicciones y Métricas
y_pred_c = knn.predict(X_test_c)
acc = accuracy_score(y_test_c, y_pred_c)
print(f"--- Métrica de Clasificación ---")
print(f"Accuracy: {acc:.4f}\n")

# Matriz de Confusión
cm = confusion_matrix(y_test_c, y_pred_c, labels=knn.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn.classes_)
fig, ax = plt.subplots(figsize=(8, 6))
disp.plot(cmap='Blues', ax=ax)
plt.title('Matriz de Confusión: KNN (k=5)')
plt.savefig('outputs/Matriz_confusion.png') 

# 2. Preparar variables de entrada estrictas: u, g, r, i, z. Objetivo: redshift
features_reg = ['u', 'g', 'r', 'i', 'z']
X_reg = df[features_reg]
y_reg = df['redshift']

# División 70/30 (aunque no lo especifica explícitamente, es buena práctica mantener la consistencia)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# Entrenar Regresión Lineal
lin_reg = LinearRegression()
lin_reg.fit(X_train_r, y_train_r)

# Predicciones y Métricas
y_pred_r = lin_reg.predict(X_test_r)
mse_val = mean_squared_error(y_test_r, y_pred_r)
r2_val = r2_score(y_test_r, y_pred_r)

with open('outputs/metricas_evaluacion.txt', 'w') as f:
    f.write(f"Accuracy KNN: {acc:.4f}\n")
    f.write(f"MSE Regresion: {mse_val:.4f}\n")
    f.write(f"R2 Regresion: {r2_val:.4f}\n")

# Gráfica de Regresión
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test_r, y=y_pred_r, alpha=0.5, color='orange')
plt.plot([y_test_r.min(), y_test_r.max()], [y_test_r.min(), y_test_r.max()], 'k--', lw=2)
plt.title('Regresión Lineal: Redshift Real vs. Predicho')
plt.xlabel('Redshift Real')
plt.ylabel('Redshift Predicho')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('outputs/Grafica_regresion.png') 

# 3. Clustering sobre magnitudes fotométricas
features_clust = ['u', 'g', 'r', 'i', 'z']
X_clust = df[features_clust]

# Aplicar KMeans con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_clust)

# Visualización comparando clusters obtenidos vs clases reales
# Usamos un par de magnitudes representativas (ej. g vs r) para el gráfico en 2D
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico 1: Clases Reales
sns.scatterplot(data=df, x='g', y='r', hue='class', palette='Set1', ax=axes[0], alpha=0.7)
axes[0].set_title('Clasificación Real (Datos Originales)')

# Gráfico 2: Clusters de KMeans
sns.scatterplot(data=df, x='g', y='r', hue='cluster', palette='viridis', ax=axes[1], alpha=0.7)
axes[1].set_title('Agrupación obtenida por KMeans (k=3)')

plt.savefig('outputs/clustering')