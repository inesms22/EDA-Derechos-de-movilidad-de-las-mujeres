# Women Mobility Rights Analysis

## 1) Objetivo

El objetivo de este proyecto es analizar y visualizar un dataset relacionado con los derechos de movilidad de las mujeres a nivel global.  
El análisis se centra en entender cómo las leyes, las políticas públicas y su implementación real influyen en la igualdad de género, así como el papel que juega el nivel económico de los países.

## 2) Dataset

- Fuente: Women, Business and the Law – Mobility Rights Index. https://www.kaggle.com/datasets/shahzadmayo/women-business-and-the-law-mobility-rights-index
- Nº filas iniciales: 201
- Nº filas tras limpieza: 177
- Nº columnas: 22

### Variables principales:

- `overall_mobility_score`: índice global de movilidad (0–100)
- `legal_frameworks_score`: calidad del marco legal
- `supportive_frameworks_score`: políticas de apoyo
- `enforcement_perceptions_score`: implementación real de derechos
- `wb_income_group`: nivel económico del país

## 3) Preguntas

- Q1: ¿Cómo se distribuyen los niveles de movilidad entre los países?
- Q2: ¿Qué relación existe entre el nivel económico y los derechos de movilidad?
- Q3: ¿Existe una diferencia entre el marco legal y su implementación real?

## 4) Data Issues & Fixes

El dataset presenta algunos problemas de calidad:

- Valores faltantes en variables relacionadas con la implementación (`enforcement_*`)
- Datos incompletos en algunos países
- Posibles inconsistencias en variables de texto

### Soluciones aplicadas:

- Eliminación de filas con valores nulos en variables clave de enforcement (24 filas eliminadas)
- Eliminación de duplicados (aunque no se detectaron)
- Limpieza de texto en variables categóricas
- Eliminación de la columna `country_code` por ser redundante ya que ya tenemos el `country_name`

## 5) Pipeline

El proyecto sigue el siguiente flujo de trabajo:
raw → clean → features → viz → export
Pasos:

1. Carga del dataset (`load_csv`)
2. Limpieza del dataset (`clean`)
3. Creación de nuevas variables en el dataset que favorecen el análisis (`build_features`)
4. Validación del dataset (`assert_columns`)
5. Visualización de las variables más interesantes para el análisis (`plot_graph`)
6. Exportación del dataset limpio a `data/processed/`

## 6) Features creadas

Se han generado nuevas variables para mejorar el análisis:

- `mobility_level`: clasificación del nivel de movilidad (High, Medium, Low)
- `legal_vs_enforcement_gap`: diferencia entre leyes y su implementación
- `rights_count`: número de derechos legales disponibles
- `enforcement_average`: media del nivel de implementación real

## 7) Visualizaciones

Se han utilizado distintos tipos de gráficos para explorar los datos:

- Histograma → distribución del mobility score
- Boxplot → comparación por nivel económico
- Gráfico de barras → distribución de niveles de movilidad
- Scatterplot → relación entre gap legal y movilidad
- Crosstab + gráfico apilado → movilidad por nivel económico
- Matrices de correlación → relaciones entre variables

## 8) Hallazgos

### 🔹 Distribución de datos

La mayoría de los países presentan puntuaciones altas en el índice de movilidad (entre 80 y 100), lo que indica un nivel elevado de igualdad a nivel global.  
Sin embargo, existe un grupo reducido de países con valores significativamente más bajos, reflejando desigualdades importantes.

### 🔹 Relación con el nivel económico

El análisis muestra una relación clara entre el nivel económico y los derechos de movilidad:

- Los países con ingresos altos presentan puntuaciones más altas y menor variabilidad
- Los países con ingresos bajos muestran mayor dispersión y niveles más bajos

Esto indica que la igualdad de género está fuertemente relacionada con el desarrollo económico.

### 🔹 Distribución de niveles de movilidad

La mayoría de los países se concentran en niveles medios y altos de movilidad, mientras que una minoría presenta niveles bajos.  
Esto sugiere que existe un progreso global, aunque no uniforme.

### 🔹 Brecha entre leyes e implementación

El análisis del scatterplot muestra que no existe una relación directa entre el marco legal y el resultado final.  
Esto indica que, aunque muchos países tienen leyes avanzadas, su aplicación no siempre es efectiva.

### 🔹 Relación economía – movilidad (crosstab)

Los datos muestran que:

- Los países de ingresos altos se concentran en niveles altos de movilidad
- Los países de bajos ingresos aparecen con mayor frecuencia en niveles bajos

Esto refuerza la relación entre desarrollo económico y derechos.

### 🔹 Correlación entre variables

La matriz de correlación muestra que:

- El índice de movilidad está fuertemente relacionado con:
  - el marco legal
  - el número de derechos
  - la implementación

- El gap entre leyes e implementación tiene baja correlación directa

Esto indica que la igualdad depende de múltiples factores combinados.

## 9) Conclusiones

El análisis permite extraer las siguientes conclusiones:

- Existe un alto nivel global de igualdad en los derechos de movilidad
- Sin embargo, persisten diferencias significativas entre países
- El nivel económico es un factor clave en la igualdad de género
- No basta con tener leyes, es necesario aplicarlas correctamente
- Factores estructurales e institucionales influyen de forma decisiva

### Conclusión final

La igualdad en los derechos de movilidad no depende únicamente del marco legal, sino también del nivel de desarrollo económico y de la capacidad de los países para implementar estas leyes de forma efectiva.

## 10) Estructura del proyecto

project/
├── main.py
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
│ └── eda.ipynb
├── src/
│ ├── **init**.py
│ ├── io.py
│ ├── cleaning.py
│ ├── config.py
│ ├── features.py
│ ├── viz.py
│ └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

## 11) Cómo ejecutar

1. Crear entorno virtual:

- python -m venv .venv
- .venv\Scripts\activate

2. Instalar dependencias:

- pip install -r requirements.txt

3. Ejecutar el pipeline:

- python main.py
