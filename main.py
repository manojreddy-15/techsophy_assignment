import yaml
import time
from src.api.stock_client import StockClient
from src.processing.data_validator import validate_data
from src.detection.anomaly_detector import AnomalyDetector
from src.alerting.alert_manager import AlertManager

def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    stocks = config['stocks']
    interval = config.get('interval_seconds', 60)

    api_client = StockClient(config['api'])
    detector = AnomalyDetector(config['anomaly'])
    alert_manager = AlertManager(config['alert'])

    print(f"Monitoring stocks: {stocks}")
    while True:
        prices = api_client.get_prices(stocks)
        valid_prices = validate_data(prices)
        print("Current prices:", valid_prices)
        anomalies = detector.detect(valid_prices)
        if anomalies:
            alert_manager.send(anomalies)
            anomalous_stocks = list(anomalies.keys())
            print("Stocks with anomalies:", anomalous_stocks)
        else:
            print("No anomalies detected.")
        time.sleep(interval)

if __name__ == "__main__":
    main()