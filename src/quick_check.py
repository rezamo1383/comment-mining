from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"
TRAIN = RAW / "train.csv"
TEST = RAW / "test.csv"

def main():
    train = pd.read_csv(TRAIN)
    test = pd.read_csv(TEST)
    print("Train shape:", train.shape)
    print("Test shape:", test.shape)
    lowers = [c.lower() for c in train.columns]
    label = None
    for key in ["label","sentiment","target","class","y"]:
        if key in lowers:
            label = train.columns[lowers.index(key)]
            break
    if label:
        print("Label distribution:")
        print(train[label].value_counts(dropna=False))

if __name__ == "__main__":
    main()