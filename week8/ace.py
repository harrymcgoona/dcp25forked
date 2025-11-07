
def clean_word(word):
    word = word.replace(",", "")
    word = word.replace("`", "")
    word = word.replace("’", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("\n", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace("'", "")
    word = word.lower().strip()
    return word

# Load the file
with open('data/aceventura.txt', 'r') as f:
    lines = f.readlines()

# Count word frequencies
word_counts = {}

for line in lines:
    words = line.split()
    for word in words:
        cleaned = clean_word(word)
        if cleaned:  # Skip empty strings
            if cleaned in word_counts:
                word_counts[cleaned] += 1
            else:
                word_counts[cleaned] = 1

# Find top 10 most common words
print("Top 10 Most Common Words:")
print("-" * 30)
top_10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

for word, count in top_10:
    print(f"{word}: {count}")
print()

# Extract character names
def extract_characters(lines):
    characters = []
    
    # Big list of stop words for screenplay formatting
    stop_words = [
        'EXT.', 'INT.', 'FADE', 'CUT', 'DISSOLVE', 'DAY', 'NIGHT', 
        'MORNING', 'AFTERNOON', 'EVENING', 'CONTINUOUS', 'LATER',
        'CONT\'D', '(CONT\'D)', 'CONTINUED', 'ANGLE', 'CLOSE', 'WIDE',
        'INSERT', 'POV', 'BACK', 'FLASHBACK', 'MONTAGE', 'SERIES',
        'ESTABLISHING', 'AERIAL', 'UNDERWATER', 'DREAM', 'SEQUENCE',
        'SUPER:', 'TITLE:', 'SUBTITLE:', 'FREEZE', 'FRAME', 'SLOW',
        'MOTION', 'TIME', 'LAPSE', 'MATCH', 'JUMP', 'SMASH', 'WIPE',
        'IRIS', 'BLACKOUT', 'WHITEOUT', 'END', 'THE', 'CREDITS',
        'ROLL', 'OVER', 'BLACK', 'WHITE', 'FADE IN:', 'FADE OUT:',
        'FADE TO:', 'CUT TO:', 'DISSOLVE TO:', 'MATCH CUT TO:',
        'JUMP CUT TO:', 'SMASH CUT TO:', 'WIPE TO:', 'IRIS IN:',
        'IRIS OUT:', 'FROM', 'ABOVE', 'BELOW', 'BEHIND', 'THROUGH',
        'ACROSS', 'ALONG', 'AROUND', 'INTERCUT', 'SPLIT', 'SCREEN'
    ]
    
    for line in lines:
        stripped = line.strip()
        
        # Check if line is all uppercase and has content
        if stripped and stripped.isupper():
            # Check if it's not a stop word or scene heading
            is_stop_word = False
            for stop in stop_words:
                if stop in stripped:
                    is_stop_word = True
                    break
            
            # Also skip if line has parentheses (like stage directions)
            # or if it's too long (probably not a character name)
            if not is_stop_word and '(' not in stripped and len(stripped) < 30:
                # Clean up the character name
                character = stripped.replace(':', '').strip()
                if character and character not in characters:
                    characters.append(character)
    
    return characters

# Get character names
characters = extract_characters(lines)

# Count lines per character
character_lines = {}
for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Check if this is a character name
    for character in characters:
        if stripped == character or stripped == character + ':':
            # Count this as a speaking line for the character
            if character in character_lines:
                character_lines[character] += 1
            else:
                character_lines[character] = 1
            break

# Character Report
print("CHARACTER REPORT")
print("=" * 40)
print(f"Total unique characters: {len(characters)}")
print("\nLines per character:")
print("-" * 30)

# Sort characters by number of lines (descending)
sorted_chars = sorted(character_lines.items(), key=lambda x: x[1], reverse=True)
for character, count in sorted_chars:
    print(f"{character}: {count} lines")

# Find character with most dialogue
if sorted_chars:
    top_character, top_count = sorted_chars[0]
    print(f"\nCharacter with most dialogue: {top_character} ({top_count} lines)")