import pandas as pd;
import matplotlib.pyplot as plt;

#Load the dataset
df=pd.read_csv("C:/Users/DELL/Licensed_Drivers.csv")
df.head()

print("Dataset Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# Drop Duplicate Rows (if any)
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# Removing Missing Values
df.fillna({"Drivers": df["Drivers"].mean()}, inplace=True)
print("\nMissing Values:\n", df.isnull().sum())

#BAR PLOT
# Group by gender and sum
gender_counts = df.groupby('Sex')['Drivers'].sum()
# Plot
gender_counts.plot(kind='bar', color=['skyblue', 'lightpink'], edgecolor='black')
plt.title('Total Licensed Drivers by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Licensed Drivers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


## Histogram
# Group by age group and sum
age_group_counts = df.groupby('Cohort')['Drivers'].sum()
# Plot
age_group_counts.sort_index().plot(kind='bar', color='orange', edgecolor='black')
plt.title('Total Licensed Drivers by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Licensed Drivers')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
