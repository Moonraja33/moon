from agent import BasicAIAgent
from dashboard import show_results, show_win_loss_graph
from data_feed import PriceSimulator
from config import get_config
import time

def run_trading_simulation(agent, price_simulator, config):
    """Run a trading simulation with the AI agent."""
    trading_config = config['trading']
    symbol = trading_config['general']['default_symbols'][0]
    update_interval = trading_config['general']['update_interval']
    max_iterations = trading_config['simulation']['max_iterations']
    
    print(f"🤖 Starting trading simulation for {symbol}")
    print(f"📊 Update interval: {update_interval} seconds")
    
    for iteration in range(max_iterations):
        # Get current market data
        market_data = price_simulator.get_real_time_price(symbol)
        current_price = market_data['price']
        
        # Generate trading signal
        signal = agent.generate_confident_signal()
        
        # Log trading activity
        print(f"\nIteration {iteration + 1}/{max_iterations}")
        print(f"Price: ${current_price:.2f}")
        print(f"Signal: {signal}")
        
        # Simulate trade execution
        if signal['action'] != 'HOLD':
            agent.execute_trade(signal, current_price)
        
        # Wait for next update
        time.sleep(update_interval)

def main():
    """Main entry point for running the AI Trading Agent."""
    # Initialize components
    config = get_config()
    agent = BasicAIAgent()
    price_simulator = PriceSimulator()
    
    print("🚀 AI Trading Agent Simulation Started...")
    print("----------------------------------------")
    
    try:
        # Run trading simulation
        run_trading_simulation(agent, price_simulator, config)
        
        # Show final results
        print("\n📈 Trading Session Results")
        print("----------------------------------------")
        show_results(agent)
        show_win_loss_graph(agent)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Simulation interrupted by user")
        show_results(agent)
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
    finally:
        print("\n✨ Simulation completed")

if __name__ == "__main__":
    main()