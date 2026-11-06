import pandas as pd

DATA_FILE = "Food_Delivery_Times.csv"

def load_clean_data():
    df = pd.read_csv(DATA_FILE)

    print("Original dataset shape:", df.shape)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove ID column because it does not help prediction
    if "Order_ID" in df.columns:
        df = df.drop(columns=["Order_ID"])

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nCleaned dataset shape:", df.shape)

    return df


def get_features_target():
    df = load_clean_data()

    X = df.drop(columns=["Delivery_Time_min"])
    y = df["Delivery_Time_min"]

    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    return X, y, numerical_features, categorical_features


if __name__ == "__main__":
    df = load_clean_data()
    print(df.head())
