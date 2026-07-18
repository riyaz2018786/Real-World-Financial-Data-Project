import pandas as pd
import numpy as np

def create_market_history():
    np.random.seed(50)
    days = 250
    
    dates = pd.date_range(start="2025-01-01", periods=days, freq='B')
    
    tech_returns = np.random.normal(0.001, 0.02, size=days)
    energy_returns = np.random.normal(0.0005, 0.015, size=days)
    
    tech_prices = 150 * np.exp(np.cumsum(tech_returns))
    energy_prices = 80 * np.exp(np.cumsum(energy_returns))
    
    data = {
        'Date': dates,
        'TechStock': np.round(tech_prices, 2),
        'EnergyStock': np.round(energy_prices, 2)
    }
    
    df = pd.DataFrame(data)
    df.to_csv('financial_market_data.csv', index=False)
    print("Market tracking history saved.")

if __name__ == "__main__":
    create_market_history()