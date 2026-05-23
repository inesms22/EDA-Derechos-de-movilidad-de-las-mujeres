from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean
from src.features import build_features
from src.utils import assert_columns
from src.viz import plot_graph


def main():
    df = load_csv(RAW_PATH)
    df = clean(df)
    df = build_features(df)
    assert_columns(df, [
        "overall_mobility_score",
        "wb_income_group",
        "mobility_level",
        "legal_frameworks_score",
        "supportive_frameworks_score",
        "enforcement_perceptions_score",
        "enforcement_average",
        "rights_count",
        "legal_vs_enforcement_gap"
    ])

    plot_graph(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
