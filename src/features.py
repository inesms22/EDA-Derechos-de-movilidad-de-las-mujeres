import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    #Variable 1. Nivel de movilidad
    df["mobility_level"] = df["overall_mobility_score"].apply(
        lambda x: "High" if x > 90 else "Medium" if x > 70 else "Low"
    )

    #Variable 2. Diferencia entre leyes e implementación
    df["legal_vs_enforcement_gap"] = df["legal_frameworks_score"] - df["enforcement_perceptions_score"]

    #Variable 3. Resume los derechos en una variable
    rights_cols = [
        "law_can_choose_where_to_live",
        "law_can_travel_internationally",
        "law_can_leave_marital_home",
        "law_equal_citizenship_rights"
    ]

    df["rights_count"] = df[rights_cols].sum(axis=1)

    #Variable 4. Resume las implementaciones reales en una variable
    enf_cols = [
        "enf_right_to_choose_where_to_live",
        "enf_right_to_travel_internationally",
        "enf_right_to_leave_marital_home",
        "enf_equal_citizenship_rights"
    ]

    df["enforcement_average"] = df[enf_cols].mean(axis=1)

    return df