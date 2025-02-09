# Importing Libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Loading the Data
data = pd.read_csv("apple_products.csv")
print(data.head())

# Checking for Null Values
print(data.isnull().sum())

# Descriptive Statistics of the Data
print(data.describe())

# Top 10 Highest-Rated iPhones
highest_rated = data.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])

# Visualizing Number of Ratings for Top 10 iPhones
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, y=counts, title="Number of Ratings of Highest Rated iPhones")
figure.show()

# Visualizing Number of Reviews for Top 10 iPhones
iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, y=counts, title="Number of Reviews of Highest Rated iPhones")
figure.show()

# Relationship Between Sale Price and Number of Ratings
figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship Between Sale Price and Number of Ratings of iPhones")
figure.show()

# Relationship Between Discount Percentage and Number of Ratings
figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship Between Discount Percentage and Number of Ratings of iPhones")
figure.show()