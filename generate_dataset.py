import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sales_data(filename='sales_data.csv'):
    np.random.seed(42)
    random.seed(42)

    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_rng = pd.date_range(start=start_date, end=end_date, freq='D')
    
    products = {
        'T-Shirts': {'price': 25.0, 'base_sales': 50, 'trend_multiplier': 0.05, 'winter_drop': True},
        'Jeans': {'price': 60.0, 'base_sales': 30, 'trend_multiplier': 0.02, 'winter_drop': False},
        'Jackets': {'price': 120.0, 'base_sales': 5, 'trend_multiplier': 0.01, 'winter_drop': False}, 
        'Dresses': {'price': 80.0, 'base_sales': 15, 'trend_multiplier': 0.03, 'winter_drop': True},
        'Accessories': {'price': 15.0, 'base_sales': 40, 'trend_multiplier': 0.04, 'winter_drop': False}
    }
    
    data = []
    
    for i, dt in enumerate(date_rng):
        day_of_week = dt.weekday()
        month = dt.month
        
        weekend_boost = 1.5 if day_of_week >= 5 else 1.0
        
        holiday_boost = 1.8 if month in [11, 12] else 1.0
        
        for category, details in products.items():
            trend = i * details['trend_multiplier']
            
            season_mult = 1.0
            if details['winter_drop'] and month in [11, 12, 1, 2]:
                season_mult = 0.5 
            if category == 'Jackets' and month in [10, 11, 12, 1, 2]:
                season_mult = 4.0 
            if category == 'Jackets' and month in [5, 6, 7, 8]:
                season_mult = 0.2 
                
            base = details['base_sales']
            noise = np.random.normal(0, base * 0.2) 
            
            units = (base + trend + noise) * weekend_boost * holiday_boost * season_mult
            units = max(0, int(units)) 
            
            price = details['price']
            revenue = units * price
            
            data.append([dt, category, units, price, revenue])

    df = pd.DataFrame(data, columns=['Date', 'Product_Category', 'Units_Sold', 'Unit_Price', 'Total_Revenue'])

    num_missing = int(len(df) * 0.01)
    missing_indices = np.random.choice(df.index, size=num_missing, replace=False)
    df.loc[missing_indices, 'Units_Sold'] = np.nan
    df.loc[missing_indices, 'Total_Revenue'] = np.nan

    df.to_csv(filename, index=False)
    print(f"Successfully generated {filename} for ARK Clothing with {len(df)} rows.")

if __name__ == '__main__':
    generate_sales_data()
