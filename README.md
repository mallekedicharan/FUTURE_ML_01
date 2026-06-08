ARK Clothing - Sales & Demand Forecasting
📌 Project Overview
The ARK Clothing Sales & Demand Forecasting project is a comprehensive data analytics and machine learning solution designed to analyze historical transaction data and forecast future sales. This predictive insight aims to optimize inventory planning across product categories, streamline staffing, and improve cash flow management.

🚀 Features
Synthetic Data Generation: Generates realistic daily sales data taking into account weekend boosts, holiday seasonality, and category-specific trends (e.g., winter jackets spike).
Data Cleaning & Preprocessing: Handles missing values using linear interpolation to ensure clean data for accurate modeling.
Key Performance Indicators (KPIs): Calculates and displays total revenue, month-over-month growth, best-selling categories, and average monthly revenue.
Interactive Visual Dashboard: A unified, dark-themed matplotlib dashboard featuring:
Revenue breakdown by category (Donut Chart)
Total units sold by category (Bar Chart)
Historical trend and future forecast dynamically plotted up to the year 2027
Time Series Forecasting: Utilizes the Holt-Winters Exponential Smoothing model (with additive trend and seasonality) to predict future unit sales accurately.
Automated Notebook Generation: Dynamically builds a complete, well-documented Jupyter Notebook containing analysis and strategic business insights.

📂 Project Structure
├── generate_dataset.py       # Script to generate synthetic 'sales_data.csv'
├── sales_data.csv            # The historical sales dataset (generated)
├── sales_forecasting.py      # Main script to run the analytics and display the unified dashboard
├── build_notebook.py         # Script to programmatically generate the Jupyter Notebook
├── sales_forecasting.ipynb   # The generated Jupyter Notebook with deep analysis
├── requirements.txt          # Python dependencies required for the project
└── README.md                 # Project documentation (this file)

🛠️ Technologies Used
Python 3
Pandas & NumPy: Data manipulation and numerical operations.
Matplotlib & Seaborn: Custom styled, dark-mode data visualization.
Statsmodels: Time series forecasting (Holt-Winters Exponential Smoothing).
Jupyter & nbformat: Programmatic notebook generation and presentation.

⚙️ Installation & Setup
1.Navigate to the project directory:
cd "ML project"
2.Install required dependencies: Make sure you have Python installed, then run:
pip install -r requirements.txt

🏃‍♂️ Usage
1. Generate the Dataset If you need to generate fresh sales data, run:
python generate_dataset.py
(This will create or overwrite sales_data.csv with simulated 3-year daily data).
2. View the Sales Dashboard To view the unified dashboard with KPIs, revenue breakdowns, and the forecast up to 2027, run:
python sales_forecasting.py
(A beautiful dark-themed dashboard will open up in a separate window).
3. Generate and View the Jupyter Notebook To programmatically build the detailed Jupyter Notebook, run:
python build_notebook.py
Once generated, you can open it using Jupyter:
jupyter notebook sales_forecasting.ipynb

📈 Strategic Insights
Revenue vs. Volume Dynamics: High-volume items (T-shirts/Accessories) drive steady foot traffic, whereas high-value seasonal items (Jackets) are primary margin drivers.
Inventory Phasing: Helps avoid overstocking in predicted dip periods while ramping up supply right before forecasted peaks.
