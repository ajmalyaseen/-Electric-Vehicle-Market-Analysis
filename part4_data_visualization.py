import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElectricCarData_Clean.csv')

# ── Chart 1: Bar chart - vehicles per manufacturer ──
brand_count = df['Brand'].value_counts()

plt.figure(figsize=(12, 6))
plt.bar(brand_count.index, brand_count.values, color='steelblue', edgecolor='black')
plt.title('Number of Vehicles per Manufacturer')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.savefig('chart1_brand_count.png', dpi=300)
plt.show()

# ── Chart 2: Histogram - price distribution ──
plt.figure(figsize=(10, 6))
plt.hist(df['PriceEuro'], bins=10, color='salmon', edgecolor='black')
plt.title('Price Distribution of Electric Cars')
plt.xlabel('Price (Euro)')
plt.ylabel('Count')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart2_price_distribution.png', dpi=300)
plt.show()

# ── Chart 3: Scatter plot - Efficiency vs Price ──
plt.figure(figsize=(10, 6))
plt.scatter(df['Efficiency_WhKm'], df['PriceEuro'],
            color='green', alpha=0.6, s=80, edgecolors='black')
plt.title('Efficiency vs Price')
plt.xlabel('Efficiency (Wh/km)')
plt.ylabel('Price (Euro)')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart3_efficiency_vs_price.png', dpi=300)
plt.show()

# ── Chart 4: Pie chart - cars by Segment ──
segment_count = df['Segment'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(segment_count.values,
        labels=segment_count.index,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True)
plt.title('Cars by Segment')
plt.tight_layout()
plt.savefig('chart4_segment_pie.png', dpi=300)
plt.show()

# ── Chart 5: Horizontal bar - top 10 efficient cars ──
top10 = df.nsmallest(10, 'Efficiency_WhKm')[['Brand', 'Model', 'Efficiency_WhKm']]
top10['Label'] = top10['Brand'] + ' ' + top10['Model']

plt.figure(figsize=(10, 6))
plt.barh(top10['Label'], top10['Efficiency_WhKm'],
         color='mediumpurple', edgecolor='black')
plt.title('Top 10 Most Efficient Cars')
plt.xlabel('Efficiency (Wh/km)')
plt.ylabel('Car')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart5_top10_efficiency.png', dpi=300)
plt.show()
