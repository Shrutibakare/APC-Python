import pandas as pd 
data ={
    "Name":["Amit","Sam","Kunal"],
    "Age" :[20,21,34],
    "Marks":[85,90,78]
}
df = pd.DataFrame(data)

print("Student Dataframes:")
print(df)

print("\nStudent Names:")
print(df["Name"])

print("\nAverage Marks:")
print(df["Marks"].mean())