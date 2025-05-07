python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data (replace 'your_data.csv' with the actual file name)
df = pd.read_csv('your_data.csv')

# Convert 'Created Date' to datetime
df['Created Date'] = pd.to_datetime(df['Created Date'])

# Check data types
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())

# Example: Value counts for 'Complaint Type'
print(df['Complaint Type'].value_counts())

# Example: Bar chart of 'Borough'
df['Borough'].value_counts().plot(kind='bar')
plt.title('Complaints by Borough')
plt.xlabel('Borough')
plt.ylabel('Number of Complaints')
plt.show()

#Example: Resolution Time by Borough
sns.boxplot(x='Borough', y='Resolution time (in days)', data=df)
plt.show()