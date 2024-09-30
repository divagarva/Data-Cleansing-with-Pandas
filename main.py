# Import necessary libraries
import pandas as pd
import numpy as np

# Sample data (You can replace this with your dataset)
data = {
    'Name': ['John Doe', 'Anna Smith', 'Peter Parker', 'John Doe', np.nan],
    'Age': [28, 22, np.nan, 28, 35],
    'Email': ['john@example.com', 'anna_smith@example.com', 'peterp@example.com', 'john@example.com', 'test_email'],
    'Join Date': ['2023-01-01', '2023-02-01', '2023/03/05', np.nan, '2022-12-15'],
    'Salary': ['50K', '40K', np.nan, '50K', '60K']
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 1: Handle Missing Data
# Fill missing 'Name' values with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

# Fill missing 'Age' with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Drop rows where 'Join Date' is missing
df = df.dropna(subset=['Join Date'])

# Step 2: Standardize Data Formats
# Convert 'Join Date' to datetime
df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')

# Standardize 'Salary' by removing 'K' and converting to numeric
df['Salary'] = df['Salary'].str.replace('K', '').astype(float) * 1000

# Step 3: Remove Duplicates
df = df.drop_duplicates()

# Step 4: Handle Inconsistent Data
# Ensure all email addresses are in lowercase
df['Email'] = df['Email'].str.lower()

# Remove rows with invalid emails (simple check for '@')
df = df[df['Email'].str.contains('@')]

# Step 5: Clean up column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Final Cleaned Data
print("\nCleaned Data:")
print(df)

# Export the cleaned data to a CSV file
df.to_csv('cleaned_data.csv', index=False)
