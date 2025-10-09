# Tutorial: Loading and Processing ABC Music Files

## What is ABC Notation?

ABC notation is a text-based music notation system used to write traditional and folk music. It's human-readable and perfect for practicing file processing in Python!

### Our Sample File: "Hunter's Purse"

```
X:283
T:Hunter's Purse, The
M:4/4
L:1/8
R:reel
K:Ador
ed|:cAAB AGEF|GFAF GFED|cBcd eged|cdef gedg|
|eAAB AGEF|GFAF GFED|cBcd eged|1 (3cBA BG A2 ed:|2 (3cBA BG A2 cd|
|:eaab aged|cdef gedB|cBcd eged|cdef gedg|
|eaab aged|cdef gedB|cBcd eged|1 (3cBA BG A2 cd:|2 (3cBA BG A4|
```

### Understanding the Structure

**Header Fields:**
- `X:` - Reference number
- `T:` - Title
- `M:` - Meter (time signature)
- `L:` - Default note length
- `R:` - Rhythm type (reel, jig, etc.)
- `K:` - Key signature (must be last header field)

**Music Notation:**
- Letters (A-G, a-g) represent notes
- `|` - Bar line
- `:` - Repeat sign
- `2` after notes - note duration
- `(3` - Triplet
- Capital letters are lower octave, lowercase are higher

---

## Step 1: Reading the File

First, let's create the ABC file and read it:

```python
# Create the ABC file
abc_content = """X:283
T:Hunter's Purse, The
M:4/4
L:1/8
R:reel
K:Ador
ed|:cAAB AGEF|GFAF GFED|cBcd eged|cdef gedg|
|eAAB AGEF|GFAF GFED|cBcd eged|1 (3cBA BG A2 ed:|2 (3cBA BG A2 cd|
|:eaab aged|cdef gedB|cBcd eged|cdef gedg|
|eaab aged|cdef gedB|cBcd eged|1 (3cBA BG A2 cd:|2 (3cBA BG A4|"""

# Save to file
with open("hunters_purse.abc", "w") as file:
    file.write(abc_content)

# Read the file
with open("hunters_purse.abc", "r") as file:
    content = file.read()
    print(content)
```

---

## Step 2: Parsing the Header

Let's extract the metadata from the header fields:

```python
def parse_abc_header(filename):
    """
    Parse the header information from an ABC file.
    Returns a dictionary with metadata.
    """
    metadata = {}
    music_lines = []
    in_header = True
    
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check if this is a header line
            if in_header and ':' in line and line[0].isalpha() and line[1] == ':':
                field = line[0]
                value = line[2:].strip()
                
                # Map field codes to readable names
                field_names = {
                    'X': 'reference',
                    'T': 'title',
                    'M': 'meter',
                    'L': 'default_length',
                    'R': 'rhythm',
                    'K': 'key'
                }
                
                if field in field_names:
                    metadata[field_names[field]] = value
                
                # K (key) is the last header field
                if field == 'K':
                    in_header = False
            else:
                # This is music notation
                music_lines.append(line)
    
    metadata['music'] = music_lines
    return metadata

# Test it
song_data = parse_abc_header("hunters_purse.abc")

print("=== Song Metadata ===")
for key, value in song_data.items():
    if key != 'music':
        print(f"{key.title()}: {value}")

print("\n=== Music Notation ===")
for line in song_data['music']:
    print(line)
```

**Output:**
```
=== Song Metadata ===
Reference: 283
Title: Hunter's Purse, The
Meter: 4/4
Default_Length: 1/8
Rhythm: reel
Key: Ador

=== Music Notation ===
ed|:cAAB AGEF|GFAF GFED|cBcd eged|cdef gedg|
|eAAB AGEF|GFAF GFED|cBcd eged|1 (3cBA BG A2 ed:|2 (3cBA BG A2 cd|
...
```

---

## Step 3: Extracting Notes

Now let's extract all the individual notes from the music:

```python
def extract_notes(music_lines):
    """
    Extract all notes from ABC music notation.
    Returns a list of notes.
    """
    notes = []
    
    for line in music_lines:
        for char in line:
            # Check if character is a note (A-G, a-g)
            if char.isalpha() and char.lower() in 'abcdefg':
                notes.append(char)
    
    return notes

# Get all notes
all_notes = extract_notes(song_data['music'])
print(f"Total notes in tune: {len(all_notes)}")
print(f"First 20 notes: {all_notes[:20]}")
```

---

## Step 4: Analyzing the Music

Let's create functions to analyze the music:

```python
def count_notes(notes):
    """Count frequency of each note."""
    note_counts = {}
    for note in notes:
        if note in note_counts:
            note_counts[note] += 1
        else:
            note_counts[note] = 1
    return note_counts

def count_bars(music_lines):
    """Count the number of bars (measures)."""
    bar_count = 0
    for line in music_lines:
        # Count bar lines (|) but not repeat signs (:)
        bar_count += line.count('|')
    return bar_count

def find_note_range(notes):
    """Find the highest and lowest notes."""
    # In ABC notation:
    # C D E F G A B (lowercase) are higher octave
    # C, D, E, F, G, A, B, (with comma or capital) are lower octave
    
    if not notes:
        return None, None
    
    # For simplicity, just find first and last alphabetically
    # (this is a simplified version)
    note_set = set(notes)
    return min(note_set), max(note_set)

def get_most_common_note(notes):
    """Find the most frequently used note."""
    counts = count_notes(notes)
    most_common = max(counts.items(), key=lambda x: x[1])
    return most_common

# Analyze the tune
notes = extract_notes(song_data['music'])

print("=== Analysis ===")
print(f"Total notes: {len(notes)}")
print(f"Number of bars: {count_bars(song_data['music'])}")
print(f"Unique notes: {len(set(notes))}")

note_counts = count_notes(notes)
print(f"\nNote frequencies:")
for note, count in sorted(note_counts.items()):
    print(f"  {note}: {count}")

most_common_note, count = get_most_common_note(notes)
print(f"\nMost common note: {most_common_note} (appears {count} times)")
```

---

## Step 5: Creating a Complete ABC Parser Class

Let's organize everything into a class:

```python
class ABCParser:
    """Parser for ABC music notation files."""
    
    def __init__(self, filename):
        self.filename = filename
        self.metadata = {}
        self.music_lines = []
        self.notes = []
        self.parse_file()
    
    def parse_file(self):
        """Parse the ABC file into metadata and music."""
        in_header = True
        
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                
                if not line:
                    continue
                
                if in_header and ':' in line and line[0].isalpha() and line[1] == ':':
                    field = line[0]
                    value = line[2:].strip()
                    
                    field_names = {
                        'X': 'reference',
                        'T': 'title',
                        'M': 'meter',
                        'L': 'default_length',
                        'R': 'rhythm',
                        'K': 'key'
                    }
                    
                    if field in field_names:
                        self.metadata[field_names[field]] = value
                    
                    if field == 'K':
                        in_header = False
                else:
                    self.music_lines.append(line)
        
        self.extract_notes()
    
    def extract_notes(self):
        """Extract all notes from music notation."""
        for line in self.music_lines:
            for char in line:
                if char.isalpha() and char.lower() in 'abcdefg':
                    self.notes.append(char)
    
    def get_title(self):
        """Get the song title."""
        return self.metadata.get('title', 'Unknown')
    
    def get_key(self):
        """Get the key signature."""
        return self.metadata.get('key', 'Unknown')
    
    def get_meter(self):
        """Get the time signature."""
        return self.metadata.get('meter', 'Unknown')
    
    def count_notes(self):
        """Count frequency of each note."""
        counts = {}
        for note in self.notes:
            counts[note] = counts.get(note, 0) + 1
        return counts
    
    def count_bars(self):
        """Count the number of bars."""
        count = 0
        for line in self.music_lines:
            count += line.count('|')
        return count
    
    def total_notes(self):
        """Get total number of notes."""
        return len(self.notes)
    
    def unique_notes(self):
        """Get number of unique notes used."""
        return len(set(self.notes))
    
    def most_common_note(self):
        """Find the most frequently used note."""
        counts = self.count_notes()
        if not counts:
            return None, 0
        return max(counts.items(), key=lambda x: x[1])
    
    def display_info(self):
        """Display all information about the tune."""
        print(f"{'='*50}")
        print(f"Title: {self.get_title()}")
        print(f"Key: {self.get_key()}")
        print(f"Meter: {self.get_meter()}")
        print(f"Rhythm: {self.metadata.get('rhythm', 'Unknown')}")
        print(f"{'='*50}")
        print(f"Total notes: {self.total_notes()}")
        print(f"Unique notes: {self.unique_notes()}")
        print(f"Number of bars: {self.count_bars()}")
        
        note, count = self.most_common_note()
        print(f"Most common note: {note} ({count} times)")
        
        print(f"\nNote distribution:")
        for note, count in sorted(self.count_notes().items()):
            bar_length = int(count / self.total_notes() * 40)
            bar = '█' * bar_length
            print(f"  {note}: {bar} {count}")
    
    def get_music_text(self):
        """Get the music notation as text."""
        return '\n'.join(self.music_lines)

# Use the parser
parser = ABCParser("hunters_purse.abc")
parser.display_info()

print("\n=== Music Notation ===")
print(parser.get_music_text())
```

---

## Step 6: Advanced Features

### Finding Patterns

```python
def find_repeated_sequences(notes, length=4):
    """Find repeated sequences of notes."""
    sequences = {}
    
    for i in range(len(notes) - length + 1):
        sequence = ''.join(notes[i:i+length])
        if sequence in sequences:
            sequences[sequence] += 1
        else:
            sequences[sequence] = 1
    
    # Return only sequences that appear more than once
    repeated = {seq: count for seq, count in sequences.items() if count > 1}
    return repeated

# Find patterns
notes = parser.notes
patterns = find_repeated_sequences(notes, length=4)

print("=== Repeated 4-Note Patterns ===")
for pattern, count in sorted(patterns.items(), key=lambda x: x[1], reverse=True):
    print(f"{pattern}: appears {count} times")
```

### Detecting Note Transitions

```python
def analyze_intervals(notes):
    """Analyze note-to-note transitions."""
    transitions = {}
    
    for i in range(len(notes) - 1):
        transition = f"{notes[i]} → {notes[i+1]}"
        transitions[transition] = transitions.get(transition, 0) + 1
    
    return transitions

# Analyze transitions
transitions = analyze_intervals(parser.notes)

print("\n=== Most Common Note Transitions ===")
sorted_transitions = sorted(transitions.items(), key=lambda x: x[1], reverse=True)
for transition, count in sorted_transitions[:10]:
    print(f"{transition}: {count} times")
```

### Checking for Specific Melodic Patterns

```python
def contains_scale_run(notes, ascending=True):
    """Check if the tune contains ascending or descending scale runs."""
    # Define scale order
    scale = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    
    runs = []
    current_run = []
    
    for i in range(len(notes) - 1):
        note1 = notes[i].lower()
        note2 = notes[i + 1].lower()
        
        if note1 in scale and note2 in scale:
            idx1 = scale.index(note1)
            idx2 = scale.index(note2)
            
            if ascending and idx2 == idx1 + 1:
                if not current_run:
                    current_run = [note1]
                current_run.append(note2)
            elif not ascending and idx2 == idx1 - 1:
                if not current_run:
                    current_run = [note1]
                current_run.append(note2)
            else:
                if len(current_run) >= 3:
                    runs.append(current_run[:])
                current_run = []
    
    if len(current_run) >= 3:
        runs.append(current_run)
    
    return runs

# Find scale runs
ascending = contains_scale_run(parser.notes, ascending=True)
descending = contains_scale_run(parser.notes, ascending=False)

print("\n=== Scale Runs ===")
if ascending:
    print(f"Ascending runs: {len(ascending)}")
    for run in ascending[:3]:  # Show first 3
        print(f"  {'→'.join(run)}")

if descending:
    print(f"Descending runs: {len(descending)}")
    for run in descending[:3]:
        print(f"  {'→'.join(run)}")
```

---

## Exercises

### Exercise 1: File Statistics
Create a function that reads multiple ABC files and generates a summary:
- Total number of tunes
- Average notes per tune
- Most common key signature
- Most common time signature

### Exercise 2: Note Duration Parser
Enhance the parser to extract note durations:
- Parse notes with duration numbers (e.g., "A2", "B4")
- Calculate total duration of the tune
- Find the longest held note

### Exercise 3: Transposer
Create a function that transposes the tune to a different key:
- Input: original key and target key
- Output: transposed music notation
- Handle both uppercase and lowercase notes

### Exercise 4: ABC to Text Converter
Create a readable text description:
```python
def abc_to_text(parser):
    """Convert ABC notation to readable text."""
    # Example output:
    # "The tune 'Hunter's Purse' is a reel in A Dorian, 
    #  written in 4/4 time. It contains 156 notes across
    #  32 bars, with 'e' being the most common note."
```

### Exercise 5: Melody Visualization
Create a simple text-based visualization:
```python
def visualize_melody(notes, width=50):
    """Create a simple ASCII visualization of the melody."""
    # Map notes to height
    # Display as a simple line graph
```

### Exercise 6: ABC File Writer
Create a function that writes ABC files:
```python
def create_abc_file(title, key, meter, notes, filename):
    """
    Create a new ABC file from scratch.
    
    Parameters:
        title: Song title
        key: Key signature
        meter: Time signature
        notes: List of notes
        filename: Output filename
    """
    # Generate proper ABC format
    # Write to file
```

---

## Complete Working Example

Here's everything put together:

```python
class ABCMusicAnalyzer:
    """Complete ABC music file analyzer."""
    
    def __init__(self, filename):
        self.parser = ABCParser(filename)
    
    def generate_report(self):
        """Generate a comprehensive analysis report."""
        print("="*60)
        print(f"ABC MUSIC FILE ANALYSIS REPORT")
        print("="*60)
        
        # Basic info
        print(f"\n📄 FILE INFORMATION")
        print(f"   Title: {self.parser.get_title()}")
        print(f"   Key: {self.parser.get_key()}")
        print(f"   Meter: {self.parser.get_meter()}")
        print(f"   Rhythm: {self.parser.metadata.get('rhythm', 'Unknown')}")
        
        # Statistics
        print(f"\n📊 STATISTICS")
        print(f"   Total Notes: {self.parser.total_notes()}")
        print(f"   Unique Notes: {self.parser.unique_notes()}")
        print(f"   Number of Bars: {self.parser.count_bars()}")
        print(f"   Notes per Bar: {self.parser.total_notes() / self.parser.count_bars():.1f}")
        
        # Most common
        note, count = self.parser.most_common_note()
        print(f"\n🎵 MOST COMMON NOTE")
        print(f"   Note: {note}")
        print(f"   Frequency: {count} times ({count/self.parser.total_notes()*100:.1f}%)")
        
        # Note distribution
        print(f"\n📈 NOTE DISTRIBUTION")
        counts = self.parser.count_notes()
        for note in sorted(counts.keys()):
            count = counts[note]
            percentage = count / self.parser.total_notes() * 100
            bar = '█' * int(percentage / 2)
            print(f"   {note}: {bar} {count} ({percentage:.1f}%)")
        
        # Patterns
        print(f"\n🔁 REPEATED PATTERNS (4 notes)")
        patterns = find_repeated_sequences(self.parser.notes, length=4)
        if patterns:
            sorted_patterns = sorted(patterns.items(), key=lambda x: x[1], reverse=True)
            for pattern, count in sorted_patterns[:5]:
                print(f"   {pattern}: {count} times")
        else:
            print("   No repeated patterns found")
        
        print("\n" + "="*60)

# Run the complete analysis
analyzer = ABCMusicAnalyzer("hunters_purse.abc")
analyzer.generate_report()
```

---

## Real-World Applications

1. **Music Education**: Analyze tunes to teach music theory
2. **Tune Collections**: Organize and categorize folk music databases
3. **Composition Analysis**: Study melodic patterns in traditional music
4. **Data Science**: Extract features for machine learning models
5. **Music Generation**: Create AI models that generate similar tunes

---

## Challenge Projects

### Project 1: ABC Music Library Manager
Create a program that:
- Loads multiple ABC files from a directory
- Indexes all tunes by title, key, rhythm
- Searches by various criteria
- Generates statistics across the collection

### Project 2: Tune Similarity Finder
Create a system that:
- Compares two tunes
- Finds common melodic patterns
- Calculates similarity score
- Suggests related tunes

### Project 3: Practice Tool
Build an application that:
- Shows measures one at a time
- Highlights repeated sections
- Identifies difficult passages (fast note transitions)
- Generates practice exercises

---

## Summary

In this tutorial, you learned:
- ✅ Read and parse ABC music notation files
- ✅ Extract metadata and music notation
- ✅ Analyze note frequencies and patterns
- ✅ Create reusable classes for file processing
- ✅ Generate statistics and reports
- ✅ Find melodic patterns and sequences

These skills apply to any structured text file format - JSON, XML, CSV, config files, and more!

**Key Python Concepts Used:**
- File I/O with context managers
- String parsing and manipulation
- Dictionaries for data storage
- Classes for code organization
- List comprehensions
- Data analysis techniques

Happy coding! 🎵🐍