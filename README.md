# Real-World Financial Data Project

An end-to-end data pipeline built to profile multi-asset market prices, process compounding yields, and calculate historical asset standard deviation anomalies.

## Project Workflow
1. Data Generation (generate_market_data.py): Generates historical stock pricing paths spanning market periods for separate sector portfolios.
2. Data Analysis (analyze_market.py): Computes compound growth values and tracks asset price swings.
3. Data Visualization (visualize_market.py): Evaluates historical pricing tracks alongside return distributions in a structured interface.

## Tech Stack
- Language: Python
- Libraries: Pandas, NumPy, Matplotlib

## Core Visual Artifacts
- Asset Price Trajectory: Evaluates price variance scales over time across high-growth and defensive assets.
- Density Return Profiling: Maps standard market distribution shifts to show sector-specific structural fluctuations.
