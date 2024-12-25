# GSS Age Visualization Project

This project is a streamlit app that allows users to explore the age distribution and household composition of respondents in the [General Social Survey (GSS)](#what-is-the-gss). The app provides a variety of filters and display options to allow users to customize the plots to their liking.

This is a continuation of my previous project, available at the link here: [gss-analysis](https://github.com/eatsfrog/gss-analysis).

## How to use the app

After opening, the app loads the plots. These plots show the age distribution and household composition of respondents in the GSS. These plots will update as you interact with the sidebar.

### Sidebar

If you click on the arrow at the top left of the screen, you can access the sidebar. Here, you will see a variety of options that allow you to subset the data and customize the plots:

- A slider that allows you to filter the data by year.
- Dropdown menus to select sex, marital status and party affiliation
- Toggles for mean, median, and peaks. Note that these toggles will only work for the age distribution plot.

## What is the GSS?

The GSS is a survey conducted by the National Opinion Research Center (NORC) at the University of Chicago. The survey has been conducted since 1972 and is designed to monitor changes in the beliefs and behaviors of Americans over time. The [data](#where-can-i-find-this-data) includes information on a wide range of topics, including demographics, attitudes, and behaviors.

## Where can I find this data?

The data used in this project is publicly available and can be downloaded from the GSS website. It is available in a variety of formats, including SPSS, Stata, and SAS. The data used in this project was taken from the Stata distribution of the data, which can be downloaded from the link here: [GSS Data](https://gss.norc.org/us/en/gss/get-the-data.html).
