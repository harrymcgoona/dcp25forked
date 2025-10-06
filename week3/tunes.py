import pandas as pd

df = pd.read_csv("data/tuneindex.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())

for i, row in df.iterrows():
    # print(row['title'])
    pass

reels = df[df['tune_type'] == 'reel']

print(f"Reels: {reels.shape}")

jigs = df[df['tune_type'] == 'jig']

print(f"Jigs: {jigs.shape}")
