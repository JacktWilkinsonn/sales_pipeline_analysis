import matplotlib.pyplot as plt
import seaborn as sns


def plot_pipeline_stage(df):

    stage_value = (
        df.groupby("stage")
        ["deal_value"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=stage_value.values,
        y=stage_value.index
    )

    plt.title("Pipeline Value by Stage")

    plt.tight_layout()

    plt.savefig(
        "../visualizations/pipeline_by_stage.png"
    )

    plt.close()


def plot_sales_rep(df):

    rep = (
        df.groupby("sales_rep")
        ["deal_value"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=rep.values,
        y=rep.index
    )

    plt.title(
        "Sales Representative Performance"
    )

    plt.tight_layout()

    plt.savefig(
        "../visualizations/sales_rep_performance.png"
    )

    plt.close()