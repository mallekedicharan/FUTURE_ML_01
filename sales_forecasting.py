import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import timedelta
import warnings

warnings.filterwarnings('ignore')

plt.style.use('dark_background')
sns.set_theme(style='darkgrid', font_scale=1.1, 
              rc={'axes.facecolor': '#0E1117', 
                  'figure.facecolor': '#0E1117', 
                  'text.color': '#E6EDF3', 
                  'axes.labelcolor': '#9DA7B3', 
                  'xtick.color': '#9DA7B3', 
                  'ytick.color': '#9DA7B3', 
                  'grid.color': '#1A212D',
                  'axes.edgecolor': '#1A212D'})

ark_primary = '#4CC9F0'
ark_palette = ['#4CC9F0', '#4895EF', '#4361EE', '#3A0CA3', '#72EFDD']

plt.rcParams.update({
    'font.family': 'sans-serif',
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'axes.titleweight': 'bold'
})

df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

df['Units_Sold'] = df.groupby('Product_Category')['Units_Sold'].transform(lambda x: x.interpolate(method='linear'))
df['Total_Revenue'] = df.groupby('Product_Category')['Total_Revenue'].transform(lambda x: x.interpolate(method='linear'))
df = df.bfill()

total_revenue = df['Total_Revenue'].sum()
monthly_revenue = df.set_index('Date').resample('ME')['Total_Revenue'].sum()
avg_monthly_sales = monthly_revenue.mean()

last_month = monthly_revenue.iloc[-2] if len(monthly_revenue) > 1 else 0
prev_month = monthly_revenue.iloc[-3] if len(monthly_revenue) > 2 else 0
growth_pct = ((last_month - prev_month) / prev_month * 100) if prev_month else 0
best_category = df.groupby('Product_Category')['Total_Revenue'].sum().idxmax()

print("-" * 40)
print(f"TOTAL REVENUE:         ${total_revenue:,.2f}")
print(f"MoM GROWTH:            {growth_pct:.2f}%")
print(f"BEST CATEGORY:         {best_category}")
print(f"AVG MONTHLY REVENUE:   ${avg_monthly_sales:,.2f}")
print("-" * 40)

category_revenue = df.groupby('Product_Category')['Total_Revenue'].sum().reset_index()
category_units = df.groupby('Product_Category')['Units_Sold'].sum().reset_index()

monthly_units = df.set_index('Date').resample('ME')['Units_Sold'].sum()

last_date = monthly_units.index[-1]
target_year = 2027
months_to_predict = max(1, (target_year - last_date.year) * 12 + (12 - last_date.month))

model = ExponentialSmoothing(monthly_units, trend='add', seasonal='add', seasonal_periods=12).fit()
forecast = model.forecast(months_to_predict)

future_dates = [last_date + pd.DateOffset(months=i) for i in range(1, months_to_predict + 1)]
forecast.index = future_dates

fig = plt.figure(figsize=(20, 16))
fig.suptitle('ARK Clothing - Analytics & Forecasting Dashboard', fontsize=28, color=ark_primary, weight='bold')

gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 1])

ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(category_revenue['Total_Revenue'], labels=category_revenue['Product_Category'], 
        autopct='%1.1f%%', startangle=140, colors=ark_palette, 
        textprops=dict(color="#E6EDF3", weight="bold"),
        wedgeprops=dict(width=0.4, edgecolor='#0E1117'))
ax1.set_title('Revenue Breakdown', pad=15)

ax2 = fig.add_subplot(gs[0, 1])
sns.barplot(data=category_units.sort_values('Units_Sold', ascending=False), 
            y='Product_Category', x='Units_Sold', palette=ark_palette, ax=ax2)
ax2.set_title('Units Sold per Category', pad=15)

ax3 = fig.add_subplot(gs[1, :])
ax3.plot(monthly_units.index, monthly_units, label='Historical', linewidth=2.5, color=ark_primary)
ax3.plot(forecast.index, forecast, label='Forecast (till 2027)', linewidth=2.5, color='#72EFDD', linestyle='--')
ax3.axvspan(monthly_units.index[-1], forecast.index[-1], color='#1A212D', alpha=0.5)

ax3.set_title('Monthly Units Sold: Trend & Forecast (Up to 2027)', fontsize=22, pad=35)
ax3.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=8.0)
plt.show()
