import pandas as pd 

data ={
    "Name":["Siya","Kavita","Manoj"],
    "Age": [23,22,30],
    "Marks":[56,78,88]
}
df = pd.DataFrame(data)

df.to_csv("students.csv",index=False)
print("CSV file created successfully.")

df2 = pd.read_csv("students.csv")

print("\nData read from CSV file:")
print(df2)

print("\nNumber of Rows and Columns:")
print(df2.shape)