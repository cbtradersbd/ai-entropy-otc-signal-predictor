from typing import Dict, Any

class OTCStreamConsumer:
    """
    Ingests sub-millisecond OTC price feeds and prepares feature vectors for regime classification.
    """
    def __init__(self, asset: str = "EURUSD_otc"):
        self.asset = asset
        self.buffer = []

    def push_tick(self, price: float) -> None:
        self.buffer.append(price)
        if len(self.buffer) > 128:
            self.buffer.pop(0)
