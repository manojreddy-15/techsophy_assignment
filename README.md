# Real-time Stock Price Anomaly Detector

## Overview
This Python application monitors selected stock prices in real time and generates alerts when unusual price patterns (anomalies) are detected.

### Features
- Real-time stock price monitoring
- Modular architecture: API client, data processing, anomaly detection, alerting
- Time series analysis: moving averages, z-score, or LSTM (deep learning)
- Handles API rate limits and missing data
- Customizable anomaly definitions (configurable thresholds)
- Supports both statistical and machine learning-based anomaly detection

## Project Structure
- `src/api/` - Stock price API client
- `src/processing/` - Data validation and preprocessing
- `src/detection/` - Anomaly detection logic (z-score, threshold, LSTM)
- `src/alerting/` - Alert generation and notification
- `main.py` - Application entry point

## Setup
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   
3. Run the application:
   ```
   python main.py
   ```

## Configuration
- Edit `config.yaml` to set stock symbols, API providers, thresholds, and alerting options.

---
