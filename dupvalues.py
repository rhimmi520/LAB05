import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'Name': ['A', 'B', 'A', 'C'],
    'Age': [20,  None, 20, 25]
})

print("Original Data:\n", df)

df = df.drop_duplicates()
df['Age'] = df['Age'].fillna(df['Age'].mean())

le = LabelEncoder()
df['Name'] = le.fit_transform(df['Name'])

print("\nFinal Data:\n", df)
