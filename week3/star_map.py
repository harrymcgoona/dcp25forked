import pandas as pd

# ============================================
# LOAD THE DATA
# ============================================

df = pd.read_csv("data/HabHYG15ly.csv", encoding='latin-1')

print(f"Loaded {len(df)} stars")

# ============================================
# ACCESSING COLUMNS
# ============================================

# Get a single column
distances = df['Distance']
x_coords = df['Xg']
y_coords = df['Yg']
z_coords = df['Zg']

# Get a single value
first_star_name = df['Display Name'][0]  # "Sol"
first_star_x = df['Xg'][0]               # 0

print(f"First star: {first_star_name} at ({first_star_x}, {df['Yg'][0]}, {df['Zg'][0]})")

# ============================================
# ITERATE THROUGH ALL ROWS (for py5 drawing)
# ============================================

# Method 1: iterrows() - most common
for index, row in df.iterrows():
    x = row['Xg']
    y = row['Yg']
    z = row['Zg']
    name = row['Display Name']
    distance = row['Distance']
    
    # In py5, you'd do something like:
    # point(x * scale, y * scale, z * scale)
    
    print(f"{name}: ({x:.2f}, {y:.2f}, {z:.2f}) - {distance} ly")

# Method 2: itertuples() - faster for large datasets
for star in df.itertuples():
    x = star.Xg
    y = star.Yg
    z = star.Zg
    # point(x, y, z)

# ============================================
# FILTERING / SELECTING SUBSETS
# ============================================

# Only stars within 5 light years
nearby = df[df['Distance'] <= 5]
print(f"\n{len(nearby)} stars within 5 light years")

for index, row in nearby.iterrows():
    print(f"{row['Display Name']}: {row['Distance']} ly")

# Only stars with proper names
named = df[df['Proper Name'].notna()]

# Only M-class stars (red dwarfs)
m_stars = df[df['Spectral Class'].str.startswith('M', na=False)]

# Multiple conditions
close_m_stars = df[(df['Distance'] <= 10) & 
                   (df['Spectral Class'].str.startswith('M', na=False))]


print("\n" + "="*50)
print("QUICK REFERENCE")
print("="*50)
print(f"Total stars: {len(df)}")
print(f"Columns: {list(df.columns)}")
print(f"\nKey columns for py5 visualization:")
print("  - Xg, Yg, Zg: 3D galactic coordinates")
print("  - Distance: distance from Sol in light years")
print("  - Display Name: star name")
print("  - Spectral Class: star type (for coloring)")
print("  - AbsMag: absolute magnitude (for sizing)")