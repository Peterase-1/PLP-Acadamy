# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set style for seaborn
sns.set(style='whitegrid')

# ------------------------
# Task 1: Load and Explore Dataset
# ------------------------

try:
    # Load Iris dataset
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    
    print("✅ Dataset loaded successfully.")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first 5 rows
print("\n📄 First 5 rows of the dataset:")
print(df.head())

# Check structure
print("\n🔍 Data Types:")
print(df.dtypes)

# Check for missing values
print("\n🧼 Missing values:")
print(df.isnull().sum())

# Clean missing values if any (none in Iris)
df = df.dropna()

# ------------------------
# Task 2: Basic Data Analysis
# ------------------------

# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# Grouping by species
print("\n📊 Mean of numerical columns grouped by species:")
grouped = df.groupby('species').mean()
print(grouped)

# Observations
print("\n🔍 Observation:")
print("• Setosa has shorter petal length and width compared to others.")
print("• Virginica generally has the largest dimensions.")

# ------------------------
# Task 3: Data Visualization
# ------------------------

# 1. Line Chart: Simulated time series of petal length
df['index'] = df.index
plt.figure(figsize=(10, 4))
sns.lineplot(data=df, x='index', y='petal length (cm)', hue='species')
plt.title('Petal Length Trend by Index')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='species', y='petal length (cm)', estimator='mean')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Sepal length vs Petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()
