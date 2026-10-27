from pathlib import Path
import pandas as pd

raw_data_path = Path("data/raw/DP05.csv")
processed_data_path = Path("data/processed/white_population_proportion.csv")

def clean_and_extract_white(filepath: Path):
    df = pd.read_csv(filepath, low_memory=False)
    percent_cols = [c for c in df.columns if c.endswith("!!Percent")]
    records = []
    for col in percent_cols:
        tract_name = col.split("!!")[0]
        raw_val = df.loc[38, col]
        percent_white = pd.to_numeric(str(raw_val).replace("%", "").strip(), errors="coerce")
        
        
