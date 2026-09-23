# Task 2: Pandas & Dataset Handling
# Name: Bandari Shravya

import pandas as pd

# 1. Create a DataFrame
print("1. Creating a DataFrame")

data = {
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 78],
    "Department": ["AI-ML", "CSE", "IT"]
}

df_demo = pd.DataFrame(data)

print(df_demo)


# 2. Load CSV Dataset
print("\n2. Loading CSV Dataset")

df = pd.read_csv("students.csv")

print(df)


# 3. Display First Rows
print("\n3. First 5 Rows")

print(df.head())


# 4. Display Last Rows
print("\n4. Last 5 Rows")

print(df.tail())


# 5. Check Rows and Columns
print("\n5. Rows and Columns")

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Shape:", df.shape)


# 6. Check Data Types
print("\n6. Data Types")

print(df.dtypes)


# 7. Basic Statistical Information
print("\n7. Statistical Information")

print(df.describe())


# 8. Select Specific Columns
print("\n8. Selected Columns")

print(df[["Name", "Marks"]])


# 9. Filter Rows Based on Condition
print("\n9. Students with Marks greater than 80")

filtered_df = df[df["Marks"] > 80]

print(filtered_df)


# 10. Additional Filtering
print("\n10. Students from AI-ML Department")

ai_ml_students = df[df["Department"] == "AI-ML"]

print(ai_ml_students)