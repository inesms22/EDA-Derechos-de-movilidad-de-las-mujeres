import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:
    # Histogram for a numerical variable
    plt.figure()
    df['overall_mobility_score'].hist(bins=20)
    plt.title("Distribución del Mobility Score")
    plt.xlabel("Score")
    plt.ylabel("Frecuencia")
    plt.show()

    # Boxplot
    plt.figure()
    df.boxplot(column="overall_mobility_score", by="wb_income_group")
    plt.title("Mobility Score por nivel de ingresos")
    plt.suptitle("")
    plt.xticks(rotation=45)
    plt.show()

    # Bar plot for a categorical variable
    plt.figure()
    df["mobility_level"].value_counts().plot(kind="bar")
    plt.title("Distribución de niveles de movilidad")
    plt.xlabel("Nivel")
    plt.ylabel("Número de países")
    plt.show()

    # Scatterplot
    plt.figure()
    sns.scatterplot(
        x="legal_vs_enforcement_gap",
        y="overall_mobility_score",
        data=df
    )
    plt.title("Relación entre gap legal y mobility score")
    plt.xlabel("Gap legal vs enforcement")
    plt.ylabel("Mobility Score")
    plt.show()

    # Crosstab for two categorical variables   
    crosstab = pd.crosstab(df["mobility_level"], df["wb_income_group"])
    print(crosstab)

    #Representación gráfica de la crosstab
    crosstab.plot(kind="bar", stacked=True)
    plt.title("Movilidad por nivel económico")
    plt.show()

    # Correlation matrix
    cols = [
        "overall_mobility_score",
        "legal_frameworks_score",
        "supportive_frameworks_score",
        "enforcement_perceptions_score",
        "enforcement_average",
        "rights_count",
        "legal_vs_enforcement_gap"
    ]

    corr = df[cols].corr()

    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matriz de correlación (variables principales)")
    plt.show()