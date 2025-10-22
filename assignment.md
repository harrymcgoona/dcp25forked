# ABC Music Dashboard
  
**Weight:** 30%
**Submission:** GitHub repository URL + In-class demo

---

## Overview

You will build a complete database application that:
1. Reads ABC music files from multiple folders (representing different books)
2. Parses and stores tunes in a MySQL database
3. Loads data into pandas for analysis
4. Create a dashboard so that a user can browse the data
5. Maintains proper version control with Git/GitHub

---

## Dataset Structure

You will receive a folder structure like this:

```
abc_books/
├── 0/
│   ├── tune001.abc
│   ├── tune002.abc
│   └── tune003.abc
├── 1/
│   ├── tune100.abc
│   ├── tune101.abc
│   └── tune102.abc
├── 2/
│   ├── tune200.abc
│   └── tune201.abc
└── 3/
    └── tune300.abc
```

- Each numbered folder represents a "book" (collection)
- Each folder contains one or more ABC files
- Each ABC file may contain one or more tunes
- Folder numbers start at 0

---

## Part 1: Database Design & File Parsing (30%)

### Design Database Schema

Create a MySQL database called `abc_music` with a table called `tunes`.

**Required columns:**
- `id` - INT, PRIMARY KEY, AUTO_INCREMENT
- `book` - INT (folder number where tune was found)
- `tune_id` - VARCHAR(20) (the X: value from ABC)
- `title` - VARCHAR(255)
- `alt_title` - VARCHAR(255) (nullable)
- `tune_type` - VARCHAR(50) (reel, jig, hornpipe, etc.)
- `key_signature` - VARCHAR(20) (G, D, Em, Ador, etc.)
- `notation` - TEXT (the complete ABC notation)

### File Discovery

Write code to discover all ABC files in the folder structure.

**Requirements:**
- Recursively traverse the `abc_books/` directory
- Identify all `.abc` files
- Determine the book number from the parent folder name
- Handle cases where folders might be named "0", "1", "2", etc.

### Parse and Insert Tunes

For each ABC file:
1. Parse all tunes in the file (using logic from previous lab)
2. Insert each tune into the database with the correct book number

---

## Part 2: Data Loading with Pandas (20%)

### Load Data from MySQL

Create a function that loads the entire tunes table into a pandas DataFrame.

```python
import pandas as pd
import mysql.connector

def load_tunes_from_database():
    """Load all tunes from MySQL into DataFrame"""
    conn = connect_to_database()
    
    query = "SELECT * FROM tunes"
    df = pd.read_sql(query, conn)
    
    conn.close()
    return df
```

### Create Analysis Functions

Write functions to analyze the data:

```python
def get_tunes_by_book(df, book_number):
    """Get all tunes from a specific book"""
    pass

def get_tunes_by_type(df, tune_type):
    """Get all tunes of a specific type"""
    pass

def search_tunes(df, search_term):
    """Search tunes by title (case insensitive)"""
    pass

def get_statistics(df):
    """Return summary statistics"""
    stats = {
        'total_tunes': len(df),
        'books': df['book'].nunique(),
        'tune_types': df['tune_type'].value_counts().to_dict(),
        'keys': df['key_signature'].value_counts().to_dict()
    }
    return stats
```

---

## Part 3: Dashboard & Interactive Elements (40%)

Create a "dashboard". It can be purely text based or use TKInter, Django, or Py5

**Suggested Layout:**

```
+------------------------------------------+
|  ABC Music Explorer                    X |
+------------------------------------------+
| Filter by Book: [Dropdown]  [Refresh]   |
| Filter by Type: [Dropdown]  [Clear]     |
| Search Title:   [________]  [Search]    |
+------------------------------------------+
|  ID | Book | Title          | Type      |
|----|------|----------------|-----------|
|  1 |  0   | Cooley's       | reel      |
|  2 |  0   | The Butterfly  | slip jig  |
|  3 |  1   | Banish...      | jig       |
|    ...                                   |
+------------------------------------------+
| Selected Tune Details:                   |
| Title: Cooley's                          |
| Type: reel      Key: Emin                |
| [View Notation]                          |
+------------------------------------------+
| Total Tunes: 1234  |  Books: 4           |
+------------------------------------------+
```

## Part 4: Documentation & Github

Your repository should have this structure:

```
abc-music-explorer/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
├── docs/
│   └── screenshots/
```

Your README must be in [this format](https://github.com/skooter500/csresources/blob/main/assignmentreadme.md):

- Use docstrings for all functions and classes
- Include type hints where appropriate
- Add comments for complex logic


## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Loading & parsing | 30% | |
| Data Analysys | 20% | |
| Dashboard & querying | 30% | |
| Github, documentation & presentation | 20% | |

## Submission Requirements

1. **GitHub Repository URL** via the submission link

### Optional Enhancements (Bonus)
- Parse the tunes and generate search keys
- Add plot visualizations (matplotlib)
- Implement edit/delete tune functionality
- Create playlist/favorites feature
- Export to PDF/MIDI