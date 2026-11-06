import matplotlib.pyplot as plt
import seaborn as sns

from data_preprocessing import load_clean_data


def run_eda():
    df = load_clean_data()

    # Basic information
    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Distribution of delivery time
    plt.figure(figsize=(8, 5))
    sns.histplot(
        df["Delivery_Time_min"].dropna(),
        bins=30,
        kde=True
    )
    plt.title("Distribution of Delivery Time")
    plt.xlabel("Delivery Time (minutes)")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig("delivery_time_distribution.png")
    plt.show()

    # Distance vs delivery time
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Distance_km",
        y="Delivery_Time_min"
    )
    plt.title("Distance vs Delivery Time")
    plt.tight_layout()
    plt.savefig("distance_vs_delivery.png")
    plt.show()

    # Traffic vs delivery time
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="Traffic_Level",
        y="Delivery_Time_min"
    )
    plt.title("Traffic Level vs Delivery Time")
    plt.tight_layout()
    plt.savefig("traffic_vs_delivery.png")
    plt.show()


if __name__ == "__main__":
    run_eda()
