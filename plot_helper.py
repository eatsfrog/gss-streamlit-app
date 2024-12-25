import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde


def plot_age_distribution(data, display_mean, display_median, display_peaks):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create KDE plot
    sns.kdeplot(data, x="age", fill=True, ax=ax)

    # Add mean
    if display_mean:
        mean = data["age"].mean()
        plt.axvline(mean, color="red", linestyle="--", label=f"Mean: {mean:.2f}")

    # Add median
    if display_median:
        median = data["age"].median()
        plt.axvline(
            median, color="green", linestyle="--", label=f"Median: {median:.2f}"
        )

    # Add peaks
    if display_peaks:

        # Calculate the KDE (numerically) for the age data
        kde = gaussian_kde(data["age"])

        # Generate a range of age values for plotting the KDE
        age_range = np.linspace(data["age"].min(), data["age"].max(), 1000)

        # Evaluate the KDE over the age range
        kde_values = kde(age_range)

        # Find peaks in the KDE values
        peaks, _ = find_peaks(
            kde_values, prominence=0.00001, height=0.005, width=5, distance=10
        )

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


def plot_household_composition(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Define the household variables and their formatted names
    household_vars = ["babies", "preteen", "teens", "adults", "unrelat"]
    formatted_names = ["Babies", "Preteen", "Teens", "Adults", "Unrelated"]

    # Group the data by household size and sum the household variables
    household_composition = data.groupby("hompop")[household_vars].sum()

    # Plot the grouped bar chart
    household_composition.plot(kind="bar", figsize=(10, 6), ax=ax)
    ax.set_title("Household Composition by Household Size")
    ax.set_xlabel("Household Size")
    ax.set_ylabel("Number of Members")
    ax.legend(labels=formatted_names, title="Household Members")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.grid(axis="y", alpha=0.5)

    return fig
