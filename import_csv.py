import pandas as pd
brands = pd.read_csv("C:/Users/hp/Downloads/Online sports revenue/brands.csv")
info = pd.read_csv("C:/Users/hp/Downloads/Online sports revenue/info.csv")
finance = pd.read_csv("C:/Users/hp/Downloads/Online sports revenue/finance.csv")
reviews = pd.read_csv("C:/Users/hp/Downloads/Online sports revenue/reviews.csv")

# Formatting the datasets for analysis
# Merging all data together
merged = brands.merge(finance, on='product_id').merge(info, on='product_id', suffixes=('nds','nfo')).merge(reviews, on='product_id', suffixes=('nds', 'ews'))
merged.dropna(inplace=True)  #dropping null values

# Sales performance of Adidas and Nike products by quartiles:
# Creating a column in the DataFrame called price_label and inputting values based on listing price quartiles
labels = ['Budget', 'Average', 'Expensive', 'Elite']
merged['price_label'] = pd.qcut(merged['listing_price'], labels=labels, q=4)

# Calculating metrics based on price_label and rounding up to 2 dec places:
# Group by price-label to get volume(count) and the mean revenue
adidas_vs_nike = merged.groupby(['brand', 'price_label'], as_index=False).agg(num_products=('product_id', 'count'), mean_revenue=('revenue', 'mean')).round(2)
print(adidas_vs_nike.head)

# To find the relationship between product description lengths, ratings, and reviews:

# Length of each product description
merged['description_length'] = merged['description'].str.len()

# Create bins for word limits and labels for description lengths:
limits = [0, 100, 200, 300, 400, 500, 600, 700] #Upper description of length limits
labels = ['100', '200', '300', '400', '500', '600', '700'] # Description of length labels

# Cut into description_length bins
merged['description_length'] = pd.cut(merged['description_length'], bins=limits, labels=labels)

# Group by bins(description_length)
description_lengths = merged.groupby('description_length', as_index=False).agg(mean_rating=('rating', 'mean'), num_reviews=('reviews', 'count')).round(2)
#print(description_lengths)
print(merged)
print(description_lengths)





