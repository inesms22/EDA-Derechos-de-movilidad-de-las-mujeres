from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw" / "WBL_Mobility_2026_ds.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_WBL_Mobility_2026_ds.csv"