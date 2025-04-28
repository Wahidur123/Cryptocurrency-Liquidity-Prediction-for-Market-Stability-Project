# Cryptocurrency Liquidity Prediction for Market Stability

## Project Overview
This project focuses on predicting the liquidity ratio of cryptocurrencies using machine learning.  
Liquidity prediction helps traders and investors understand how easily a cryptocurrency can be bought or sold, ensuring market stability.

## Workflow Summary
- Data Collection: CoinGecko data for March 16-17, 2022.
- Data Cleaning: Handling missing values and duplicates.
- Feature Engineering: Created moving averages, volatility, and liquidity ratio.
- Exploratory Data Analysis (EDA): 
  - Bitcoin Price Trend
  - Correlation Heatmap
- Model Building:
  - Linear Regression (baseline model)
  - Random Forest Regressor (final model after hyperparameter tuning)
- Evaluation Metrics:
  - RMSE
  - MAE
  - R² Score (achieved **0.87** after tuning)
- Model Saving: Saved the trained model (`liquidity_prediction_model.pkl`) using Joblib.
- Local Deployment: Streamlit app deployed using Ngrok for public access.

## Folder Structure
- `source_code/`: Jupyter notebook (.ipynb) with full code
- `eda_report/`: EDA images and statistics table
- `model/`: Trained model (.pkl file)
- `deployment/`: Streamlit app file (`app.py`)
- `documents/`: Final Report, HLD, LLD, Pipeline Architecture documents

## Technologies Used
- Python, Pandas, Numpy
- Scikit-learn, Streamlit, Joblib
- Ngrok (for local app deployment)

## Deployment Link
(App was deployed locally using Streamlit + Ngrok during testing.)

## Author
- Wahidur Rahaman

