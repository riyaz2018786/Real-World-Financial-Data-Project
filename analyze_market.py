import pandas as pd
import numpy as np

def process_metrics():
    df = pd.read_csv('financial_market_data.csv')
    
    tech_pct = df['TechStock'].pct_change().dropna()
    energy_pct = df['EnergyStock'].pct_change().dropna()
    
    tech_total_return = ((df['TechStock'].iloc[-1] - df['TechStock'].iloc[0]) / df['TechStock'].iloc[0]) * 100
    energy_total_return = ((df['EnergyStock'].iloc[-1] - df['EnergyStock'].iloc[0]) / df['EnergyStock'].iloc[0]) * 100
    
    tech_volatility = tech_pct.std() * np.sqrt(252) * 100
    energy_volatility = energy_pct.std() * np.sqrt(252) * 100
    
    print("--- TOTAL PERFORMANCE RETURNS ---")
    print(f"Tech Asset Return: {tech_total_return:.2f}%")
    print(f"Energy Asset Return: {energy_total_return:.2f}%")
    
    print("\n--- ANNUALIZED ASSET RISK PROFILE ---")
    print(f"Tech Stock Volatility: {tech_volatility:.2f}%")
    print(f"Energy Stock Volatility: {energy_volatility:.2f}%")

if __name__ == "__main__":
    process_metrics()