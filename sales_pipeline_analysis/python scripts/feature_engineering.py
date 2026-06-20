import pandas as pd


def add_features(df):

    today = pd.Timestamp.today()

    df["pipeline_age_days"] = (
        today - df["created_date"]
    ).dt.days

    df["days_since_last_interaction"] = (
        today - df["last_interaction_date"]
    ).dt.days

    bins = [
        0,
        10000,
        500000,
        1000000,
        5000000,
        100000000,
        float("inf")
    ]

    labels = [
        "0-10K",
        "10K-500K",
        "500K-1M",
        "1M-5M",
        "5M-100M",
        "100M+"
    ]

    df["size_bucket"] = pd.cut(
        df["deal_value"],
        bins=bins,
        labels=labels
    )

    df["forecast_month"] = (
        df["expected_close_date"]
        .dt.to_period("M")
        .astype(str)
    )

    df["stale_opportunity"] = (
        df["days_since_last_interaction"] > 30
    )

    return df