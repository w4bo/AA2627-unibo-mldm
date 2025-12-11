import pandas as pd
import numpy as np

# Step 1: Create the sales dataframe
sales_data = {
    'ID': [1, 2, 3, 4, 5],
    'ProductID': [101, 102, 103, 101, 104],
    'PriceBin': ['Low', 'Medium', 'High', 'Low', 'Low'],
    'Date': ['10/01/2024', '10/02/2024', '10/03/2024', '10/04/2024', '10/05/2024'],
    'Quantity': [5, 10, np.nan, 20, 15]
}

sales_df = pd.DataFrame(sales_data)

# Step 2: Create the products dataframe
products_data = {
    'productid': [101, 102, 103, 104],
    'ProductName': ['Product A', 'Product B', 'Product C', 'Product D']
}

products_df = pd.DataFrame(products_data)

# Step 3: Handle missing values in sales_df using fillna()
sales_df['Quantity'].fillna(sales_df['Quantity'].mean(), inplace=True)  # Fill missing Quantity with mean value

# Step 4: Convert Date to Unix timestamp
sales_df['Date'] = pd.to_datetime(sales_df['Date'], format='%m/%d/%Y')
sales_df['UnixTimestamp'] = sales_df['Date'].astype(int) / 10**9  # Convert to Unix timestamp

# Step 5: Calculate Total Sales based on PriceBin mapping
price_map = {'Low': 10, 'Medium': 20, 'High': 30}
sales_df['TotalSales'] = sales_df['Quantity'] * sales_df['PriceBin'].map(price_map)

# Step 6: Ordinal encode PriceBin
sales_df['PriceBinEncoded'] = sales_df['PriceBin'].map({'Low': 1, 'Medium': 2, 'High': 3})

# Step 7: Scale Quantity using Min-Max Normalization
sales_df['QuantityScaled'] = (sales_df['Quantity'] - sales_df['Quantity'].min()) / (sales_df['Quantity'].max() - sales_df['Quantity'].min())

# Step 8: Join sales_df with products_df on ProductID
final_df = sales_df.merge(products_df, how='left', left_on='ProductID', right_on='productid')

# Step 9: Print the final dataframe
print(final_df)
