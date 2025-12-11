import pandas as pd

# Step 1: Create the DataFrame with columns Name, Age, and City
data = [["Alice", 20, "New York"], 
        ["Bob", 21, "Los Angeles"], 
        ["Charlie", 19, "New York"]]
df = pd.DataFrame(data, columns=["Name", "Age", "City"])

data = {
    "Name": ["Alice", "Bob", "Charlie" ],
    "Age": [20, 21, 19],
    "City": ["New York", "Los Angeles", "New York"]
}
df = pd.DataFrame(data)

# Step 2: Select and print the column Name
name_column = df['Name']
print("Column 'Name':")
print(name_column)

# Step 3: Filter the DataFrame to show rows where Age is greater/equal than 20
age_filtered_df = df[df['Age'] >= 20]
print("\nRows where Age is greater or equal to 20:")
print(age_filtered_df)

# Step 4: Add a new column 'Year' which is 2024 minus the Age
df['Year'] = 2024 - df['Age']

# Step 5: Group the DataFrame by City and calculate the average Age for each city
city_grouped = df.groupby('City')['Age'].mean()
print("\nAverage Age per City:")
print(city_grouped)

# Step 6: Sort the DataFrame by Age in descending order
sorted_df = df.sort_values(by='Age', ascending=False)

# Step 7: Export the final DataFrame to a CSV file
sorted_df.to_csv("mt_df.csv", index=False)