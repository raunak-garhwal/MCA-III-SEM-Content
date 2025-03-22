import pandas as pd
import matplotlib.pyplot as plt

# ✅ Step 1: Load Population Data from CSV
df = pd.read_csv("ML-Programs/Raunak-ML/Population.csv")

# ✅ Step 2: Sort Data for Better Visualization
df = df.sort_values(by="Population", ascending=False).head(15)  # Top 15 countries

# ✅ Step 3: Create a Bar Graph
plt.figure(figsize=(12, 6))
plt.bar(df["Country"], df["Population"], color='skyblue', edgecolor='black')
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (in millions)", fontsize=12)
plt.title("Top 15 Most Populated Countries", fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate country names for better visibility
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add population values above bars
for i, val in enumerate(df["Population"]):
    plt.text(i, val + 5, str(val), ha='center', fontsize=10, color='black')

plt.show()

# ✅ Step 4: Create a Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df["Population"], labels=df["Country"], autopct='%1.1f%%', 
        colors=plt.cm.Paired.colors, startangle=140, textprops={'fontsize': 10})
plt.title("Population Distribution of Top 15 Countries", fontsize=14)
plt.show()
