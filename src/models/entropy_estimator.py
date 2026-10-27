import math
from typing import List, Dict, Any

class EntropyEstimator:
    """
    Estimates Shannon Information Entropy on rolling price delta distributions.
    """
    @staticmethod
    def compute_entropy(prices: List[float]) -> float:
        if len(prices) < 5:
            return 1.0
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        up = sum(1 for d in deltas if d > 0)
        down = sum(1 for d in deltas if d < 0)
        total = up + down
        if total == 0 or up == 0 or down == 0:
            return 0.1
        p_up = up / total
        p_down = down / total
        return - (p_up * math.log2(p_up) + p_down * math.log2(p_down))
