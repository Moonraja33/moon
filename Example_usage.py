# Example usage
performance_data = {
    'loss': [0.5, 0.4, 0.3, 0.2, 0.1],
    'accuracy': [0.6, 0.7, 0.8, 0.85, 0.9]
}
calculate_performance(performance_data)

agent = TradingAgent(max_memory_size=100)
result = agent.analyze("Found a potential Order Block at price level 1.2345")
agent.self_improve()

def analyze_text_command(self, text):
    text = text.lower()

    if "trend" in text:
        return "The market trend depends on higher highs or lower lows."

    elif "liquidity" in text:
        return "Liquidity zones are often targets for smart money."

    elif "structure" in text:
        return "Structure shows how the market is moving — like BOS or MSS."

    elif "strategy" in text or "suggestion" in text:
        return self.suggest_strategy()

    elif "timeframe" in text:
        return self.multi_timeframe_analysis()

    else:
        return "Sorry, I don't understand that trading concept yet."

def suggest_strategy(self):
    return (
        "Here's a suggested strategy: Use Break of Structure (BOS) with Fair Value Gap (FVG) confirmation "
        "on the 1H timeframe. Enter at discount zone, exit at premium zone."
    )

def multi_timeframe_analysis(self):
    return (
        "Analyzing multiple timeframes:\n"
        "- 1D shows uptrend\n"
        "- 4H shows retracement\n"
        "- 1H shows potential entry zone near liquidity\n"
        "Align all before entering the trade."
    )

# Test code
agent = TradingAgent()
print(agent.analyze_text_command("help"))
print("\n")
print(agent.analyze_text_command("trend"))
print("\n")
print(agent.analyze_text_command("liquidity"))