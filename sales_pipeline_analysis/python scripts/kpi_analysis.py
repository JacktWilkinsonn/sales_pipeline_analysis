def total_pipeline_value(df):
    return df["deal_value"].sum()


def average_deal_size(df):
    return df["deal_value"].mean()


def opportunity_count(df):
    return len(df)


def partner_share(df):

    partner_value = (
        df[df["partner_involved"] == "Yes"]
        ["deal_value"]
        .sum()
    )

    total_value = df["deal_value"].sum()

    return partner_value / total_value


def win_rate(df):

    wins = (
        df["stage"] == "Closed Won"
    ).sum()

    return wins / len(df)