import pandas as pd
petal = pd.read_csv(r"C:\Users\camjh\Downloads\INFO 2\Petal_Data.csv")
sepal = pd.read_csv(r"C:\Users\camjh\Downloads\INFO 2\Sepal_Data.csv")

print(petal)
print(sepal)

df = pd.merge(sepal, petal, on=['sample_id', 'species'], how='inner')
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Convert numeric columns to float!
numeric_cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

correlations = df[numeric_cols].corr()

means = df.groupby("species")[numeric_cols].mean()

medians = df.groupby("species")[numeric_cols].median()

stds = df.groupby("species")[numeric_cols].std()

summary = df.groupby("species")[numeric_cols].agg(['mean', 'median', 'std'])
print(summary)
