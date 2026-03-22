# ⚡ Electric Vehicle Market Analysis

Exploratory data analysis on a real-world dataset of 
103+ electric vehicles across 30+ brands using Python, 
Pandas, and Matplotlib.

## Problem It Solves
With hundreds of EVs in the market, comparing performance, 
efficiency, and pricing across brands is overwhelming. 
This analysis extracts clear insights from raw data — 
helping understand what actually makes an EV good value.

## Key Insights Found
- Tesla dominates with 13 unique models in the dataset
- Lightyear One is the most energy-efficient EV (104 Wh/km)
- AWD powertrains have 42% more range than FWD on average
- RapidCharge cars cost 2x more on average (€57k vs €26k)
- Strong negative correlation (-0.8) between acceleration 
  and top speed — faster cars are also quicker

## Analysis Structure
- Part 1: Performance & Efficiency Analysis
- Part 2: Market & Brand Analysis  
- Part 3: Comparative Analysis (PowerTrain, BodyStyle)
- Part 4: Data Visualization (5 charts)
- Part 5: Use Case Queries

## Visualizations
- Bar chart: Number of vehicles per manufacturer
- Histogram: Price distribution across all EVs
- Scatter plot: Efficiency vs Price relationship
- Pie chart: Cars by body segment
- Horizontal bar: Top 10 most efficient EVs

## Tech Stack
- **Language:** Python
- **Data Analysis:** Pandas
- **Visualization:** Matplotlib
- **Dataset:** ElectricCarData_Clean.csv (103 EVs)

## Setup
1. Clone the repo
   git clone https://github.com/ajmalyaseen/ev-market-analysis

2. Install dependencies
   pip install pandas matplotlib

3. Run analysis
   python part1_performance_efficiency.py
   python part2_market_brand_analysis.py
   python part3_comparative_analysis.py
   python part4_data_visualization.py
   python part5_usecase_queries.py
```

---

Now do this:

**1. Create GitHub repo** → name it `ev-market-analysis`

**2. Create project folder on laptop, add:**
- All 5 `.py` files
- `ElectricCarData_Clean.csv`
- `README.md` (paste above)
- `.gitignore` with:
```
__pycache__/
*.pyc
.venv/
.env