# Real Estate Valuation in Mazowsze

## Overview
This project aims to build a Machine Learning model to estimate secondary market real estate prices in the Mazowieckie Voivodeship (Poland). The data was originally scraped from the Otodom portal (1251 observations). 

The primary business goal is to help real estate agents, investors, and individual buyers evaluate property prices and identify overvalued or undervalued listings.

## Current Status: Work in Progress (WIP)
The project is currently under active development. I am at the data preprocessing and cleaning stage. 

**Completed so far:**
* **Feature Engineering:** Extracting and calculating new features such as the distance from the Warsaw city center (based on coordinates) and building age (`dataset.py`).
* **Data Validation:** Identifying and handling incorrect data entries (e.g., negative age values).
* **Outlier Detection:** Utilizing the IQR (Interquartile Range) method and market logic to filter out extreme anomalies in price, area, and building height.
* **Missing Values Handling:** Imputing missing data using median, mode, and grouped means depending on the variable type. Dropping columns with excessive missing data (e.g., window types).

**Upcoming next steps:**
* Comprehensive Data Visualization (EDA).
* Data Processing Pipeline (Scikit-Learn `ColumnTransformer`, encoding, and scaling).
* Machine Learning Modeling & Hyperparameter Tuning.

## Technologies Used
* **Python**
* **Pandas & NumPy** - Data manipulation and cleaning
* *(Planned)* **Matplotlib & Seaborn** - Data Visualization
* *(Planned)* **Scikit-Learn** - Machine Learning models and pipelines

## Project Structure
* `dataset.py` - Script for initial data parsing and feature engineering.
* `raport.ipynb` - Main Jupyter Notebook containing the core analysis, data cleaning, and future ML models.
* `dataset_csv.csv` / `dataset_xlsx.xlsx` - Processed tabular data ready for analysis.
