# Description: This is a Streamlit app that visualizes the age distribution of the General Social Survey (GSS) dataset. It uses a subset of the GSS dataset that contains information on age, sex, marital status, and political party. The app allows users to filter the data by year range and observe how the age distribution changes.
# Author: Ian Roman

# Import libraries
import streamlit as st
import pandas as pd
from plot_helper import (
    plot_age_distribution,
    plot_household_composition,
)  # Custom functions saved in plot_helper.py


# Load and prepare data
@st.cache_data
def load_data():
    age_data = pd.read_csv("age_dist.csv")
    return age_data


def main():
    st.title("General Social Survey Visualization App")

    st.write(
        "This app visualizes the age distribution and household composition of the General Social Survey (GSS) dataset. On the sidebar there are multiple display options to filter the data and customize the visualization."
    )

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

    # Display options for age distribution plot included in a submenu in the sidebar
    st.sidebar.subheader("Age Distribution Options")
    display_mean = st.sidebar.checkbox("Show Mean", value=False)
    display_median = st.sidebar.checkbox("Show Median", value=False)
    display_peaks = st.sidebar.checkbox("Show Peaks", value=False)

    # Filter data by year range
    data = gss[(gss["year"] >= year_range[0]) & (gss["year"] <= year_range[1])]

    # Filter data based on user inputs
    if marital_status != "All":
        data = data[data["marital"] == marital_status]

    if sex != "All":
        data = data[data["sex"] == sex]

    if partyid != "All":
        data = data[data["partyid"] == partyid]

    # Create and display plot
    fig1 = plot_age_distribution(data, display_mean, display_median, display_peaks)
    fig2 = plot_household_composition(data)

    # Display plots
    st.subheader("Age Distribution")
    st.write(
        "Age is an important demographic variable that can paint a general picture of the population. It is shown below as a KDE (Kernel Density Estimate), which is a smoothed version of a histogram with probabilities instead of counts."
    )
    st.pyplot(fig1, clear_figure=True)

    st.subheader("Household Composition")
    st.write(
        "The household composition tells us about how people are living together. Each bar represents different categories of members in a household. The graph shows household size as the x-axis and the category count as the y-axis."
    )
    st.pyplot(fig2, clear_figure=True)


if __name__ == "__main__":
    main()
