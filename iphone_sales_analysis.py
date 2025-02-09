# Import Libraries
import pandas as pd
import numpy as np
import plotly.express as px

# Generate Mock Data (if you don't have the CSV)
# ----------------------------------------------
np.random.seed(42)
num_entries = 100

data = {
    "Product Name": [f"iPhone {np.random.randint(8, 15)} (Color {i})" for i in range(num_entries)],
    "Star Rating": np.round(np.random.uniform(4.0, 5.0, num_entries), 1),
    "Number Of Ratings": np.random.randint(500, 50000, num_entries),
    "Number Of Reviews": np.random.randint(50, 5000, num_entries),
    "Sale Price": np.random.randint(30000, 150000, num_entries),
    "Discount Percentage": np.random.randint(0, 30, num_entries),
    "Mrp": np.random.randint(35000, 160000, num_entries)
}

df = pd.DataFrame(data)

# Save to CSV (optional)
# df.to_csv("apple_products.csv", index=False)

# Load Data
# ----------------------------------------------
# If you have the CSV, use:
# df = pd.read_csv("apple_products.csv")

# Data Analysis
# ----------------------------------------------
print("First 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDescriptive stats:")
print(df.describe())

# Top 10 Highest-Rated iPhones
# ----------------------------------------------
highest_rated = df.sort_values(by="Star Rating", ascending=False).head(10)
print("\nTop 10 iPhones:")
print(highest_rated[['Product Name', 'Star Rating']])

# Visualizations
# ----------------------------------------------
# Plot 1: Number of Ratings for Top 10 iPhones
fig1 = px.bar(
    highest_rated,
    x='Product Name',
    y='Number Of Ratings',
    title='Top 10 iPhones by Ratings'
)
fig1.show()

# Plot 2: Relationship between Sale Price and Number of Ratings
fig2 = px.scatter(
    df,
    x='Number Of Ratings',
    y='Sale Price',
    size='Discount Percentage',
    trendline='ols',
    title='Sale Price vs. Ratings'
)
fig2.show()

# Plot 3: Discount vs. Ratings
fig3 = px.scatter(
    df,
    x='Number Of Ratings',
    y='Discount Percentage',
    size='Sale Price',
    trendline='ols',
    title='Discount vs. Ratings'
)
fig3.show()
