import pandas as pd


def clean_data(df):
    """
    Basic CRM data cleaning
    """

    df = df.drop_duplicates()

    date_cols = [
        "created_date",
        "last_interaction_date",
        "expected_close_date"
    ]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    df["stage"] = df["stage"].str.strip()

    return df


if __name__ == "__main__":

    df = pd.read_csv("../data/raw/sales_pipeline_raw.csv")

    df = clean_data(df)

    df.to_csv(
        "../data/processed/sales_pipeline_clean.csv",
        index=False
    )

    print("Cleaning complete")