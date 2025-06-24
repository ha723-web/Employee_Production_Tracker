import pandas as pd
import matplotlib.pyplot as plt

# Load the Kaggle dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Filter to avoid division by zero
df = df[df["TotalWorkingYears"] > 0]

# Calculate Productivity Score
df["ProductivityScore"] = df["MonthlyIncome"] / df["TotalWorkingYears"]

# Display top 10 employees by productivity
top = df.sort_values(by="ProductivityScore", ascending=False)[["EmployeeNumber", "Department", "MonthlyIncome", "TotalWorkingYears", "ProductivityScore"]]

print("\n🏆 Top 10 Employees by Productivity Score (MonthlyIncome / TotalWorkingYears):\n")
print(top.head(10))

# Plot
top10 = top.head(10)
plt.figure(figsize=(10, 5))
plt.bar(top10["EmployeeNumber"].astype(str), top10["ProductivityScore"], color="blue")
plt.title("Top 10 Employee Productivity Scores")
plt.xlabel("Employee Number")
plt.ylabel("Income per Year of Experience")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("kaggle_productivity_chart.png")
plt.show()
