import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde


def plot_age_distribution(
    data, marital_status, sex, partyid, display_mean, display_peaks, display_median
):
    fig, ax = plt.subplots()

    # Filter data based on user inputs
    if marital_status != "All":
        data = data[data["marital"] == marital_status]

    if sex != "All":
        data = data[data["sex"] == sex]

    if partyid != "All":
        data = data[data["partyid"] == partyid]

    # Create KDE plot
    sns.kdeplot(data, x="age", fill=True, ax=ax)

    # Add mean, median, and peaks to plot, if selected
    if display_mean:
        mean = data["age"].mean()
        plt.axvline(mean, color="red", linestyle="--", label=f"Mean: {mean:.2f}")

    if display_median:
        median = data["age"].median()
        plt.axvline(
            median, color="green", linestyle="--", label=f"Median: {median:.2f}"
        )

    if display_peaks:
        # Calculate the KDE (numerically) for the age data
        kde = gaussian_kde(data["age"])

        # Generate a range of age values for plotting the KDE
        age_range = np.linspace(data["age"].min(), data["age"].max(), 1000)

        # Evaluate the KDE over the age range
        kde_values = kde(age_range)

        # Find peaks in the KDE values
        peaks, _ = find_peaks(kde_values, prominence=0.0000000001, wlen=3, distance=5)

        # Add peaks to plot
        for peak in peaks:
            plt.axvline(
                age_range[peak],
                color="purple",
                linestyle="--",
                label=f"Peak: {age_range[peak]:.2f}",
            )

    # Add legend if any of the display options are selected
    if display_mean or display_peaks or display_median:
        plt.legend()

    # Set plot title and labels
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Density")

    return fig
