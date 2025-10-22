"""
ABC Music File Parser - SOLUTION
Parses ABC notation files and analyzes Irish traditional music tunes
"""

import pandas as pd
import re

# ============================================
# PART 2: READ FILE INTO A LIST
# ============================================

def load_abc_file(filename):
    """Load ABC file into list of lines"""
    with open(filename, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    return lines


# ============================================
# PART 3: PARSE TUNES INTO DICTIONARIES
# ============================================

def parse_tune(tune_lines):
    """Parse a single tune from lines into a dictionary"""
    tune = {
        'X': None,
        'title': None,
        'alt_title': None,
        'tune_type': None,
        'key': None,
        'notation': '\n'.join(tune_lines)
    }
    
    title_count = 0
    
    for line in tune_lines:
        line = line.strip()
        
        if line.startswith('X:'):
            # Extract tune ID number
            tune['X'] = line[2:].strip()
            
        elif line.startswith('T:'):
            # First T: is title, second is alt_title
            if title_count == 0:
                tune['title'] = line[2:].strip()
                title_count += 1
            elif title_count == 1:
                tune['alt_title'] = line[2:].strip()
                
        elif line.startswith('R:'):
            # Extract tune type, handling comments and extra text
            r_text = line[2:].strip()
            
            # Remove comments (anything after % or #)
            if '%' in r_text:
                r_text = r_text.split('%')[0].strip()
            if '#' in r_text:
                r_text = r_text.split('#')[0].strip()
            
            # Remove text in parentheses
            r_text = re.sub(r'\([^)]*\)', '', r_text).strip()
            
            # Take first word only
            tune['tune_type'] = r_text.split()[0] if r_text else None
            
        elif line.startswith('K:'):
            # Extract key signature, removing comments and extra text
            k_text = line[2:].strip()
            
            # Remove comments
            if '%' in k_text:
                k_text = k_text.split('%')[0].strip()
            
            # Take first word/token
            tune['key'] = k_text.split()[0] if k_text else None
    
    return tune


def parse_all_tunes(lines):
    """Parse all tunes from lines"""
    tunes = []
    current_tune_lines = []
    in_tune = False
    blank_count = 0
    
    for line in lines:
        # Check if this line starts a new tune
        if line.strip().startswith('X:'):
            # If we were already collecting a tune, save it
            if current_tune_lines:
                tune = parse_tune(current_tune_lines)
                if tune['title']:  # Only add if we got a title
                    tunes.append(tune)
            
            # Start new tune
            current_tune_lines = [line]
            in_tune = True
            blank_count = 0
            
        elif in_tune:
            # Check if this is a blank line (end of tune)
            if line.strip() == '':
                blank_count += 1
                # Two consecutive blank lines means tune is definitely over
                if blank_count >= 2:
                    if current_tune_lines:
                        tune = parse_tune(current_tune_lines)
                        if tune['title']:
                            tunes.append(tune)
                    current_tune_lines = []
                    in_tune = False
                    blank_count = 0
            else:
                # Non-blank line, keep collecting
                blank_count = 0
                current_tune_lines.append(line)
    
    # Don't forget the last tune!
    if current_tune_lines:
        tune = parse_tune(current_tune_lines)
        if tune['title']:
            tunes.append(tune)
    
    return tunes


# ============================================
# PART 4 & 5: ANALYSIS FUNCTIONS
# ============================================

def analyze_tune_types(df):
    """Analyze tune types with counts and percentages"""
    print("\n" + "="*60)
    print("TUNE TYPE ANALYSIS")
    print("="*60)
    
    type_counts = df['tune_type'].value_counts()
    
    print(f"\nTotal unique tune types: {df['tune_type'].nunique()}")
    print(f"\nTune type distribution:")
    print("-" * 50)
    
    for tune_type, count in type_counts.items():
        percentage = (count / len(df)) * 100
        print(f"{tune_type:20s} {count:4d} tunes ({percentage:5.1f}%)")
    
    print("-" * 50)
    print(f"{'TOTAL':20s} {len(df):4d} tunes")
    
    return type_counts


def analyze_keys(df):
    """Analyze musical keys with counts"""
    print("\n" + "="*60)
    print("KEY SIGNATURE ANALYSIS")
    print("="*60)
    
    key_counts = df['key'].value_counts()
    
    print(f"\nTotal unique keys: {df['key'].nunique()}")
    print(f"\nTop 15 most common keys:")
    print("-" * 50)
    
    for key, count in key_counts.head(15).items():
        percentage = (count / len(df)) * 100
        print(f"{key:10s} {count:4d} tunes ({percentage:5.1f}%)")
    
    # Analyze major vs minor
    major_keys = key_counts[key_counts.index.str.contains('maj|Maj', na=False, regex=True)].sum()
    minor_keys = key_counts[key_counts.index.str.contains('min|Min|m$', na=False, regex=True)].sum()
    
    print("\n" + "-" * 50)
    print(f"Major keys: {major_keys} tunes")
    print(f"Minor keys: {minor_keys} tunes")
    print(f"Other/Modal: {len(df) - major_keys - minor_keys} tunes")
    
    return key_counts


def find_alcoholic_drinks(df):
    """Find tunes mentioning alcoholic drinks"""
    print("\n" + "="*60)
    print("TUNES MENTIONING ALCOHOLIC DRINKS")
    print("="*60)
    
    # List of drink-related terms
    drinks = [
        'whiskey', 'whisky', 'beer', 'ale', 'wine', 'brandy', 
        'punch', 'porter', 'rum', 'gin', 'bottle', 'drink',
        'drinking', 'drunk', 'drunken', 'liquor', 'toddy'
    ]
    
    # Create pattern for case-insensitive search
    pattern = '|'.join(drinks)
    
    # Find matching tunes
    drink_tunes = df[df['title'].str.contains(pattern, case=False, na=False)]
    
    print(f"\nFound {len(drink_tunes)} tunes mentioning drinks:")
    print("-" * 50)
    
    # Show the tunes
    for idx, row in drink_tunes.iterrows():
        tune_type = row['tune_type'] if pd.notna(row['tune_type']) else 'unknown'
        key = row['key'] if pd.notna(row['key']) else 'unknown'
        print(f"{row['title']:40s} ({tune_type}, {key})")
    
    # Count which drinks appear most
    print("\n" + "-" * 50)
    print("Drink mentions breakdown:")
    drink_counts = {}
    for drink in drinks:
        count = df['title'].str.contains(drink, case=False, na=False).sum()
        if count > 0:
            drink_counts[drink] = count
    
    for drink, count in sorted(drink_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {drink:15s}: {count} tune(s)")
    
    return drink_tunes


def generate_summary_statistics(df):
    """Generate overall summary statistics"""
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    print(f"\nTotal tunes: {len(df)}")
    print(f"Tunes with alternate titles: {df['alt_title'].notna().sum()}")
    print(f"Unique tune types: {df['tune_type'].nunique()}")
    print(f"Unique keys: {df['key'].nunique()}")
    
    # Title length statistics
    df['title_length'] = df['title'].str.len()
    print(f"\nTitle length statistics:")
    print(f"  Average: {df['title_length'].mean():.1f} characters")
    print(f"  Shortest: {df['title_length'].min()} characters")
    print(f"  Longest: {df['title_length'].max()} characters")
    
    # Find longest and shortest titles
    longest = df.loc[df['title_length'].idxmax()]
    shortest = df.loc[df['title_length'].idxmin()]
    
    print(f"\n  Longest title: '{longest['title']}'")
    print(f"  Shortest title: '{shortest['title']}'")


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Main program execution"""
    
    print("="*60)
    print("ABC MUSIC FILE PARSER")
    print("="*60)
    
    # Part 2: Load file
    print("\nLoading ABC file...")
    filename = 'dmi_tunes.abc'  # Change this to your filename
    
    try:
        lines = load_abc_file(filename)
        print(f"✓ Loaded {len(lines):,} lines from file")
        
        # Show first few lines
        print("\nFirst 10 lines:")
        print("-" * 50)
        for i, line in enumerate(lines[:10], 1):
            print(f"{i:3d}: {line.rstrip()}")
        
    except FileNotFoundError:
        print(f"✗ Error: Could not find file '{filename}'")
        print("Please make sure the file is in the same directory as this script.")
        return
    
    # Part 3: Parse tunes
    print("\n" + "="*60)
    print("PARSING TUNES")
    print("="*60)
    
    tunes = parse_all_tunes(lines)
    print(f"\n✓ Successfully parsed {len(tunes)} tunes")
    
    # Show first tune
    print("\nFirst tune parsed:")
    print("-" * 50)
    for key, value in tunes[0].items():
        if key == 'notation':
            print(f"{key:12s}: {value[:100]}..." if len(value) > 100 else f"{key:12s}: {value}")
        else:
            print(f"{key:12s}: {value}")
    
    # Show last tune
    print("\nLast tune parsed:")
    print("-" * 50)
    for key, value in tunes[-1].items():
        if key == 'notation':
            print(f"{key:12s}: {value[:100]}..." if len(value) > 100 else f"{key:12s}: {value}")
        else:
            print(f"{key:12s}: {value}")
    
    # Part 4: Create DataFrame
    print("\n" + "="*60)
    print("CREATING DATAFRAME")
    print("="*60)
    
    df = pd.DataFrame(tunes)
    
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    print("\nFirst 5 rows:")
    print(df[['X', 'title', 'tune_type', 'key']].head())
    
    print("\nData types:")
    print(df.dtypes)
    
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Part 5: Analysis
    type_counts = analyze_tune_types(df)
    key_counts = analyze_keys(df)
    drink_tunes = find_alcoholic_drinks(df)
    generate_summary_statistics(df)
    
    # Export results
    print("\n" + "="*60)
    print("EXPORTING RESULTS")
    print("="*60)
    
    # Export main DataFrame
    output_file = 'parsed_tunes.csv'
    df.to_csv(output_file, index=False)
    print(f"\n✓ Exported full dataset to: {output_file}")
    
    # Export drink tunes
    if len(drink_tunes) > 0:
        drink_file = 'tunes_with_drinks.csv'
        drink_tunes.to_csv(drink_file, index=False)
        print(f"✓ Exported drink tunes to: {drink_file}")
    
    # Export summary statistics
    summary_file = 'tune_statistics.txt'
    with open(summary_file, 'w') as f:
        f.write("ABC Music File Analysis Summary\n")
        f.write("="*60 + "\n\n")
        f.write(f"Total tunes: {len(df)}\n")
        f.write(f"Unique tune types: {df['tune_type'].nunique()}\n")
        f.write(f"Unique keys: {df['key'].nunique()}\n\n")
        
        f.write("Tune Types:\n")
        f.write("-"*40 + "\n")
        for tune_type, count in type_counts.items():
            f.write(f"{tune_type:20s} {count:4d}\n")
        
        f.write("\n\nTop 10 Keys:\n")
        f.write("-"*40 + "\n")
        for key, count in key_counts.head(10).items():
            f.write(f"{key:10s} {count:4d}\n")
    
    print(f"✓ Exported statistics to: {summary_file}")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    print(f"\nProcessed {len(df)} tunes from {filename}")
    print(f"Results saved to:")
    print(f"  - {output_file}")
    print(f"  - {drink_file}")
    print(f"  - {summary_file}")


if __name__ == "__main__":
    main()