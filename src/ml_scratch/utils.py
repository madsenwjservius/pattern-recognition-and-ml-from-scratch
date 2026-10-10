from pathlib import Path
import pandas as pd
import numpy as np

def get_project_root() -> Path:
    """Returns the root directory of the project."""
    # Assuming ml_from_scratch/utils.py is inside src/, the root is two level up
    return Path(__file__).resolve().parent.parent.parent

def load_csv_dataset(filename: str, target_column: int = -1, header: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """
    Loads a dataset from the data/ directory and splits it into features (X) and target (y).

    Parameters:
    -----------
    filename : str
        The name of the CSV file (e.g., 'dataset.csv' or 'processed/clean_data.csv').
    target_column : int, default=-1
        The index of the target column (default is the last column).
    header : int, default=0
        Row number to use as the column names.

    Returns:
    --------
    X : np.ndarray
        Feature matrix.
    y : np.ndarray
        Target vector.
    """
    root_dir = get_project_root()
    file_path = root_dir / "data" / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {file_path}")
    
    # Load dataset using pandas
    df = pd.read_csv(file_path, header=header)
    
    # Separate features and target
    if target_column == -1 or target_column == df.shape[1] - 1:
        X = df.iloc[:, :-1].to_numpy()
        y = df.iloc[:, -1].to_numpy()
    else:
        y = df.iloc[:, target_column].to_numpy()
        X = df.drop(df.columns[target_column], axis=1).to_numpy()
        
    return X, y