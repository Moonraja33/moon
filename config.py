import os
from typing import Dict, Any

def get_config() -> Dict[str, Any]:
    return {
        "trading": {
            "forex_pairs": ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD"],
            "default_symbol": "EUR/USD"
        },
        "ict": {
            "market_structure": {
                "bullish_bias": 0.5,
                "types": ["BOS", "MSS", "CHoCH"]
            },
            "order_blocks": {
                "reversal_threshold": 0.0020,
                "types": ["Bullish OB", "Bearish OB"]
            }
        }
    }