import pandas as pd
School  = {"class": ["A", "B", "B", "A"], "Marks": [85, 90, 78, 92]}
df  = pd.DataFrame(School)
grouped = df.groupby("class")

for class_name,  in grouped:
    print(class_name)
   
