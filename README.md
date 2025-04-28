# Trading Agent

A simple trading agent implementation using machine learning to predict market movements.

## Features
- Data loading from Yahoo Finance
- Random Forest-based prediction model
- Basic trading metrics calculation
- Caching support for financial data

## Usage
```python
from trading_agent import TradingAgent

# Initialize agent
agent = TradingAgent(symbol='AAPL')

# Train the model
agent.train(start_date='2020-01-01', end_date='2023-12-31')

# Make predictions
predictions = agent.predict(current_data)
```

## Requirements
- Python 3.7+
- pandas
- numpy
- scikit-learn
- yfinance

## Installation
```bash
pip install -r requirements.txt
```