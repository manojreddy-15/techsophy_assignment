import numpy as np

class AnomalyDetector:
    def __init__(self, config):
        self.method = config.get('method', 'zscore')
        self.zscore_threshold = config.get('zscore_threshold', 3.0)
        self.moving_average_window = config.get('moving_average_window', 20)
        self.history = {}
        self.min_history = 5
        self.change_threshold = 0.03
        self.abs_change_threshold = 10  

    def detect(self, prices):
        anomalies = {}
        for symbol, price in prices.items():
            series = self.history.setdefault(symbol, [])
            series.append(price)
            if len(series) > self.moving_average_window:
                series.pop(0)
            if len(series) > 1 and series[-2] > 0:
                pct_change = (price - series[-2]) / series[-2]
                abs_change = abs(price - series[-2])
                if abs(pct_change) >= self.change_threshold and abs_change >= self.abs_change_threshold:
                    anomalies[symbol] = price
                    continue
            if self.method == 'zscore' and len(series) > max(self.moving_average_window, self.min_history):
                window = series[:-1] if len(series) > 1 else series
                avg = np.mean(window)
                deviation = np.std(window)
                if deviation > 0 and abs(price - avg) / deviation > self.zscore_threshold:
                    anomalies[symbol] = price
        return anomalies