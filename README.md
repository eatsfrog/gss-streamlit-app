# GSS Age Visualization Project

This project is a visualization of the [General Social Survey (GSS)](#what-is-the-gss) data on age. It is a streamlit app that allows user to explore the age distribution of the respondents, allowing for different kinds of filters and display options. This is a continuation of my previous project, available at the link here: [gss-analysis](https://github.com/eatsfrog/gss-analysis).

## How to use the app

After opening, the app loads a density plot of the age distribution of respondents. If you click on the arrow at the top left of the screen, you can access the sidebar. Here, you will see a slider that allows you to filter the data by year. You can also subset the data by sex, marital status and party affiliation, using the respective dropdown menus. Finally, you can also choose whether to show the mean, median, and peaks on the graph. The app will update the plot based on the filters you select.

## What is the GSS?

The GSS is a survey conducted by the National Opinion Research Center (NORC) at the University of Chicago. The survey has been conducted since 1972 and is designed to monitor changes in the beliefs and behaviors of Americans over time. The [data](#where-to-find-the-data) includes information on a wide range of topics, including demographics, attitudes, and behaviors.

## Where can I find this data?

The data used in this project is publicly available and can be downloaded from the GSS website. It is available in a variety of formats, including SPSS, Stata, and SAS. The data used in this project is in Stata format and can be downloaded from the following link: [GSS Data](https://gss.norc.org/us/en/gss/get-the-data.html).

Once you've downloaded the data, place it in the same directory as the data_processing.py file. Then enter your terminal and run the following command: `python data_processing.py`. This will generate a processed version of the data that can be used in the app.
