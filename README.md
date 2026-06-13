# Real Estate Valuation in Mazowsze

## Overview
This project aims to build a Machine Learning model to estimate secondary market real estate prices in the Mazowieckie Voivodeship (Poland). The data was originally scraped from the Otodom portal (1251 observations). 

The primary business goal is to help real estate agents, investors, and individual buyers evaluate property prices and identify overvalued or undervalued listings.

## Project Steps Done
* **Data Validation:** Fixed negative values and corrected text variables into numbers.
* **Outlier Detection:** Removed extreme, unrealistic records using the IQR method and market logic.
* **Missing Values Imputation:** Filled empty spaces using logical averages, medians, or most frequent values, and dropped columns with too many gaps.
* **Data Visualization:** Created charts to check data distributions and look for trends between variables.
* **Data Pipeline:** Built an automated system to encode, scale, and prepare the final data for the model.

## Technologies Used
* **Python**
* **Pandas & NumPy** - Data manipulation and cleaning.
* **Matplotlib & Seaborn** - Data Visualization.
* **Scikit-Learn** - Machine Learning pipelines, scaling, and models.
* **XGBoost** - Advanced gradient boosting algorithm (the winning model).

## Project Structure
* `dataset.py` - Script for initial data parsing and feature engineering.
* `raport.ipynb` - Main Jupyter Notebook containing the core analysis, data cleaning, and future ML models.
* `dataset_csv.csv` - Processed tabular data ready for analysis.
