class AlertManager:
    def __init__(self, config):
        self.method = config.get('method', 'console')

    def send(self, anomalies):
        if self.method == 'console':
            for symbol, price in anomalies.items():
                print(f"ALERT: Anomaly detected for {symbol} at price {price}")