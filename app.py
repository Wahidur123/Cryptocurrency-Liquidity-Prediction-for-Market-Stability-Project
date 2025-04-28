import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('liquidity_prediction_model.pkl')

# Title
st.title('Cryptocurrency Liquidity Prediction App')

# Description
st.write('Enter cryptocurrency details to predict the Liquidity Ratio.')

# Input fields
price = st.number_input('Price (USD)', value=50000.0)
volume_24h = st.number_input('24h Volume (USD)', value=100000000.0)
market_cap = st.number_input('Market Cap (USD)', value=1000000000.0)
returns = st.number_input('Returns (%)', value=0.5)

# Only calculate volatility
volatility = abs(returns)

# Predict
if st.button('Predict Liquidity'):
    input_features = np.array([[price, volume_24h, market_cap, volatility]])  # Only 4 features
    liquidity_ratio = model.predict(input_features)[0]
    st.success(f'Predicted Liquidity Ratio: {liquidity_ratio:.6f}')
