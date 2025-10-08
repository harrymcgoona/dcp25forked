import pandas as pd

df = pd.read_csv("data/tuneindex.csv")

pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

def print_df(df:pd.DataFrame):
    col_count = df.shape[1]
    for i, row in df.iterrows():
        for j in range(col_count):
            print(row[j], end = "\t")
        print()

for i, row in df.iterrows():
    # print(row['title'])
    pass

reels = df[df['tune_type'] == 'reel']

print(f"Reels: {reels.shape}")

jigs = df[df['tune_type'] == 'jig']

print(f"Jigs: {jigs.shape}")

emin_tunes = df[df['key_sig'] == 'Emin']

print(f"EMinor tunes: {emin_tunes.shape}")

popular = df[df['downloaded'] > 1000]
print(popular.head())
# print_df(popular)

unpopular_hornpipes = df[(df['tune_type'] == 'hornpipe') & (df['downloaded'] < 500)]

print(unpopular_hornpipes.head())

# Group by

tune_counts = df['tune_type'].value_counts()

for key in tune_counts.keys():
    print(f"{key}\t{tune_counts[key]}")

type_key_stats = df.groupby(['tune_type', 'key_sig'])

# print(type_key_stats.count())

## sorting
least_popular = df.sort_values('downloaded')

print_df(least_popular.head())

most_popular = df.sort_values('downloaded', ascending=False)

print_df(most_popular.head())

has_reel = df[df['title'].str.contains('Reel', case=False, na=False)]

df[df['title'].str.contains('Reel', na=False)]

# Startswith
df[df['name'].str.startswith('The', na=False)]

# Endswith  
df[df['file'].str.endswith('.csv', na=False)]

# Match (regex)
df[df['notation'].str.match(r'X:\d+', na=False)]

result = pd.merge(df1, df2, on='column_name')


## Joining
import pandas as pd

# Inner join (default)
result = pd.merge(df1, df2, on='column_name')

# Left join
result = pd.merge(df1, df2, on='column_name', how='left')

# Right join
result = pd.merge(df1, df2, on='column_name', how='right')

# Outer join (full outer)
result = pd.merge(df1, df2, on='column_name', how='outer')

# Join on multiple columns
result = pd.merge(df1, df2, on=['col1', 'col2'])

df['column'].unique() → list of unique values
df.drop_duplicates() → remove duplicate rows
df['column'].nunique()