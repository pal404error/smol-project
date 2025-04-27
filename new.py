import pandas as pd

# Load the single CSV file
file_path = 'pp-monthly.csv'  # <-- replace this with your actual file name
df = pd.read_csv(file_path, header=None, quotechar='"')

# Set proper column names
df.columns = [
    'Transaction ID', 'Price', 'Date', 'Postcode', 'Property Type', 'New Build',
    'Tenure', 'PAON', 'SAON', 'Street', 'Locality', 'Town/City', 'District',
    'County', 'PPD Category', 'Record Status'
]

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'].str[:10], format='%Y-%m-%d')

# Filter for standard residential transactions only (Category 'A')
df = df[df['PPD Category'] == 'A']

# Define Prime Central London postcodes
pcl_postcodes = ['W1', 'SW1', 'SW3', 'SW5', 'SW7', 'SW10', 'NW1', 'WC1', 'WC2', 'W2', 'W8']

# Extract postcode district (first part)
df['Postcode District'] = df['Postcode'].str.extract(r'^([A-Z]{1,2}\d[A-Z]?)')

# Filter by PCL postcodes
pcl_df = df[df['Postcode District'].isin(pcl_postcodes)]

# Select only required columns
output_df = pcl_df[['Postcode', 'Price', 'Date']]

# Rename columns to match output requirement
output_df.columns = ['Postcode', 'Selling Price', 'Transaction Date']

# Save to new CSV
output_df.to_csv('land_registry_sales.csv', index=False)

print("Saved 'land_registry_sales.csv' successfully!")
