import matplotlib.pyplot as plt
import pandas as pd

def draw_market_dashboard():
    df = pd.read_csv('financial_market_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(df['Date'], df['TechStock'], color='teal', label='Tech Stock Portfolio')
    axes[0].plot(df['Date'], df['EnergyStock'], color='crimson', label='Energy Stock Portfolio')
    axes[0].set_title('Asset Price Trajectory Over Time')
    axes[0].set_xlabel('Timeline')
    axes[0].set_ylabel('Valuation Price ($)')
    axes[0].legend()
    axes[0].tick_params(axis='x', rotation=30)
    
    tech_returns = df['TechStock'].pct_change().dropna()
    energy_returns = df['EnergyStock'].pct_change().dropna()
    
    axes[1].hist(tech_returns, bins=30, alpha=0.6, color='teal', label='Tech Returns')
    axes[1].hist(energy_returns, bins=30, alpha=0.6, color='crimson', label='Energy Returns')
    axes[1].set_title('Daily Return Density Profiling')
    axes[1].set_xlabel('Return Spread Percentage')
    axes[1].set_ylabel('Density Occurrence')
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_market_dashboard()