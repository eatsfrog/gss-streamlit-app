# Description: This is a Streamlit app that visualizes the age distribution of the General Social Survey (GSS) dataset. It uses a subset of the GSS dataset that contains information on age, sex, marital status, and political party. The app allows users to filter the data by year range and observe how the age distribution changes.
# Author: Ian Roman

# Import libraries
import streamlit as st
import pandas as pd
from plot_helper import plot_age_distribution  # Custom function saved in plot_helper.py


# Load and prepare data
@st.cache_data
def load_data():
    age_data = pd.read_csv("age_dist.csv")
    return age_data


def main():
    st.title("GSS Age Distribution Visualization")

    # Load data
    gss = load_data()

    # Create sidebar
    st.sidebar.header("Controls")

    # Year range slider
    year_options = sorted(gss["year"].unique())
    year_range = st.sidebar.select_slider(
        "Select Year Range",
        options=year_options,
        value=(year_options[0], year_options[-1]),
    )

    # Dropdowns for sex, marital status, and party ID
    sex = st.sidebar.selectbox("Select Sex", ["All"] + list(gss["sex"].unique()))
    marital_status = st.sidebar.selectbox(
        "Select Marital Status", ["All"] + list(gss["marital"].unique())
    )
    partyid = st.sidebar.selectbox(
        "Select Party ID", ["All"] + list(gss["partyid"].unique())
    )

    # Display options
    display_mean = st.sidebar.checkbox("Show Mean", value=False)
    display_median = st.sidebar.checkbox("Show Median", value=False)
    display_peaks = st.sidebar.checkbox("Show Peaks", value=False)

    # Filter data by year range
    filtered_data = gss[(gss["year"] >= year_range[0]) & (gss["year"] <= year_range[1])]

    # Create and display plot
    fig = plot_age_distribution(
        filtered_data,
        marital_status,
        sex,
        partyid,
        display_mean,
        display_peaks,
        display_median,
    )

    # Display plot, clear figure after displaying
    st.pyplot(fig, clear_figure=True)


if __name__ == "__main__":
    main()
