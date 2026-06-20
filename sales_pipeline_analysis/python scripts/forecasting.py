import pandas as pd


def monthly_forecast(df):

    forecast = (
        df.groupby("forecast_month")
        ["deal_value"]
        .sum()
        .reset_index()
        .sort_values("forecast_month")
    )

    return forecast