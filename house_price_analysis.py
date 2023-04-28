import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('House Price India.csv')

# Univariate Analysis
plt.boxplot(df['living area'])
plt.show()

plt.hist(df['Price'], bins=20)
plt.show()

# Bivariate Analysis
plt.scatter(df['living area'], df['Price'])
plt.show()

# Multivariate Analysis
plt.scatter(df['living area'], df['Price'], c=df['number of bedrooms'])
plt.colorbar()
plt.show()

# Descriptive statistics
print(df.describe())

# Handle missing values
df.dropna(inplace=True)
