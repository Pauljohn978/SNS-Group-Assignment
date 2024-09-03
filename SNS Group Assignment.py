#!/usr/bin/env python
# coding: utf-8

# 4. Given a dataset with missing values and inconsistencies, clean and prepare the data for analysis. 

# In[14]:


#Extracting dataset from local desktop
import pandas as pd

# Define the path to the Excel file
excel_file_path = 'D:/Black Coffer/archives/Superstore.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the first few rows of the DataFrame
print(df.head())


# In[15]:


#Checking for Null Values

missing_values = df.isnull()

# Count missing values per column
missing_count = df.isnull().sum()

print(missing_count)


# In[ ]:


#Checking for inconsistencies

# Check values less than zero in Row ID
print(df['Row ID'].unique())

# Count unique values
df['Row ID'].value_counts()

# Filter inconsistent values (e.g., negative ages in an 'Age' column)
inconsistent_values = df[df['Row ID'] < 0]
print(inconsistent_values)


# In[23]:


# Defining the pattern for Order ID
pattern = r'^[A-Z]{2}-\d{4}-\d{6}$'

# Check for values matching the pattern in the 'ids' column
non_matching_values = df[~df['Order ID'].str.match(pattern, na=False)]

# Print matching values
print("Matching Values:\n", non_matching_values)


# In[28]:


valid_ship_modes = ['First Class', 'Second Class', 'Standard Class','Same Day']

# Check for values not in the list of valid ship modes
non_matching_ship_modes = df[~df['Ship Mode'].isin(valid_ship_modes)]

# Print non-matching ship modes
print("Non-Matching Ship Modes:\n", non_matching_ship_modes)


# In[30]:


valid_segments = ['Consumer', 'Corporate', 'Home Office']

# Check for values not in the list of valid ship modes
non_matching_segments = df[~df['Segment'].isin(valid_segments)]

# Print non-matching ship modes
print("Non-Matching Segments:\n", non_matching_segments)


# In[32]:


valid_directions = ['North', 'South', 'East', 'West', 'Central']

# Check for values not in the list of valid ship modes
non_valid_directions = df[~df['Region'].isin(valid_directions)]

# Print non-matching ship modes
print("Non-Matching Regions:\n", non_valid_directions)


# In[35]:


valid_category = ['Furniture', 'Office Supplies', 'Technology']

# Check for values not in the list of valid ship modes
non_valid_category = df[~df['Category'].isin(valid_category)]

# Print non-matching ship modes
print("Non-Matching Category:\n", non_valid_category)


# 5. Perform a statistical analysis on a given dataset to identify significant trends and correlations. Provide a summary of your findings. 

# In[36]:


#Extracting dataset from local desktop
import pandas as pd

# Define the path to the Excel file
excel_file_path = 'D:/Black Coffer/archives/Superstore.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Display the first few rows of the DataFrame
print(df.head())


# In[37]:


# Mean, median, standard deviation, etc.
mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
std_sales = df['Sales'].std()

print(f'Mean Sales: {mean_sales}, Median Sales: {median_sales}, Std Sales: {std_sales}')


# In[ ]:





# In[ ]:




