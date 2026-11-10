from pathlib import Path
import pandas as pd

# Find the dataset folder
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "dataset" / "raw"

# Find CSV and Excel files
files = sorted(
    list(data_folder.glob("*.csv")) +
    list(data_folder.glob("*.xlsx"))
)

if not files:
    print("No CSV or Excel dataset found in dataset/raw.")
else:
    print("Available datasets:")
    for number, file in enumerate(files, start=1):
        print(number, file.name)

    # Read the first dataset
    file = files[0]

    if file.suffix.lower() == ".csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    print("\nDataset loaded:", file.name)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset size (rows, columns):")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())