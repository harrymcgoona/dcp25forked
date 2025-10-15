import pandas as pd

df = pd.read_csv("data/tuneindex.csv")

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

print(df.head()) # print the first 5
print(df.tail()) # print last 5
print(df.shape) # rows and cols

print(df.columns)


df1 = pd.read_csv("data/album.csv")

altan = df1[df1['artist'] == 'Altan']

print(altan.shape[0])

uni = df1[df1['artist'].notnull()]

uni = df1['artist'].unique()

print(len(uni))

print(uni)

for i in range(len(uni)):
    print(uni[i])

df2 = pd.read_csv("data/albumtracktune.csv")

lonesome = df2[df2['album_id'] == 1]

for i in range(len(lonesome)):
    print(f"{lonesome['title'][i]}  {lonesome['track_num'][i]} {lonesome['tune_num'][i]}")

print(lonesome['title'][len(lonesome) - 1])


for c in df.columns:
    print(c)
print("info:")
print(df.info())

print("describe:")

print(df.describe())


def print_df(df, count):
    for i, row in df.iterrows():
        print(row['title'])
        
        for c in df.columns:
            print(row[c])
        if i == 50:
            break

def print_df1(df, count):
    rows = df.shape[0]
    for i in range(rows):
        print(df['title'][i])


# print_df(df, 100)

# print_df1(df, 100)

reels = df[df['tune_type'] == 'reel'] # 

print("reels:")
print(reels.shape)

for i, row in reels.iterrows():
    print(f"{i} {row['title']}")

emin = df[df['key_sig'] == 'EMin']

maids = df[df['title'].str.contains("maid", case= False)]

print("maid tunes")
print(maids.shape[0])

# for i, row in maids.iterrows():
#    print(row['title'])


print("e minor tunes")
print(emin.shape[0])
# print_df1(reels, 50)

popular_tunes = df[df['downloaded'] > 1000]

print_df(popular_tunes, 10)

sorted = df.sort_values('downloaded', ascending=False)


#for i, row in sorted.iterrows():
#    print(f"{i} {row['title']} {row['downloaded']}")
    
# print(sorted.head())

tunes_by_type = df.groupby("tune_type")


# print(tunes_by_type.head())

# print_df(sorted, 10)



