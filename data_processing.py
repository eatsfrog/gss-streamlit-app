# This script processes the General Social Survey (GSS) dataset to extract and clean the relevant columns for the analysis.

# Import the necessary libraries
import numpy as np
import pandas as pd


# Define a function to clean and convert columns
def clean_and_convert_columns(dataframe):
    dataframe = dataframe.copy()

    column_names = dataframe.columns.tolist()

    for column in column_names:
        if dataframe[column].dtype == "object":
            dataframe[column] = dataframe[column].str.strip()  # strip whitespace
            dataframe[column] = dataframe[column].str.replace(
                r"\.[a-z]", "NaN", regex=True
            )  # Encode missing values properly
            dataframe[column] = (
                dataframe[column].replace("NaN", np.nan).astype("Int64")
            )  # Convert to numeric values
    return dataframe


# Define mappings for marital status, party ID, and sex
marital_status_mapping = {
    1.0: "Married",
    2.0: "Widowed",
    3.0: "Divorced",
    4.0: "Separated",
    5.0: "Never married",
}

partyid_simplified_mapping = {
    0.0: "Democrat",
    1.0: "Democrat",
    2.0: "Other",
    3.0: "Other",
    4.0: "Other",
    5.0: "Republican",
    6.0: "Republican",
    7.0: "Other",
}

sex_mapping = {1.0: "Male", 2.0: "Female"}

# Load the GSS dataset
data = pd.read_stata("gss.dta", convert_categoricals=False)

# Apply the function to clean and convert columns
gss_data = clean_and_convert_columns(data)

# Filter the dataset to include only the relevant columns
gss_data = gss_data[["year", "age", "sex", "marital", "partyid"]]

# Apply the mappings
gss_data["marital"] = gss_data["marital"].map(marital_status_mapping)
gss_data["partyid"] = gss_data["partyid"].map(partyid_simplified_mapping)
gss_data["sex"] = gss_data["sex"].map(sex_mapping)

# Drop NAs
gss_data.dropna(inplace=True)

# Save the processed dataset
gss_data.to_csv("age_dist.csv", index=False)
