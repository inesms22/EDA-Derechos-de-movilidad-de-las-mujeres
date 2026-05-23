import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    
    #Eliminar datos duplicados (aunque en este dataset no hay)
    df = df.drop_duplicates()

    #Eliminar las filas con valores nulos en variables de enforcement
    df = df.dropna(subset=[
        "enforcement_perceptions_score",
        "enf_right_to_choose_where_to_live",
        "enf_right_to_travel_internationally",
        "enf_right_to_leave_marital_home",
        "enf_equal_citizenship_rights"
    ])

    #Limpiar el texto
    df["country_name"] = df["country_name"].str.strip()
    df["wb_region"] = df["wb_region"].str.strip()
    df["wb_income_group"] = df["wb_income_group"].str.strip()

    #Eliminar la columna del código del país ya que es innecesaria
    df = df.drop(columns=["country_code"], errors="ignore")

    return df