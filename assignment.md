# ABC Music Database & GUI Assignment
## Building a Traditional Irish Music Database Explorer

**Due Date:**   
**Weight:** 35%
**Submission:** GitHub repository URL + In-class demo

---

## Overview

You will build a complete database application that:
1. Reads ABC music files from multiple folders (representing different books)
2. Parses and stores tunes in a MySQL database
3. Loads data into pandas for analysis
4. Provides a tkinter GUI for browsing and searching the tune collection
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

### Task 1.1: Design Database Schema

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

### Task 1.2: File Discovery

Write code to discover all ABC files in the folder structure.

**Requirements:**
- Recursively traverse the `abc_books/` directory
- Identify all `.abc` files
- Determine the book number from the parent folder name
- Handle cases where folders might be named "0", "1", "2", etc.

### Task 1.3: Parse and Insert Tunes

For each ABC file:
1. Parse all tunes in the file (using logic from previous lab)
2. Insert each tune into the database with the correct book number
3. Handle duplicate tunes gracefully

---

## Part 2: Data Loading with Pandas (15%)

### Task 2.1: Load Data from MySQL

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

### Task 2.2: Create Analysis Functions

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

## Part 3: Tkinter GUI (40%)

### Task 3.1: Main Window Design

Create a tkinter application with the following components:

**Layout:**
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

### Task 3.2: Required Features

**1. Data Display (15%)**
- Display tunes in a scrollable table (Treeview widget)
- Show columns: ID, Book, Title, Type, Key
- Initially load all tunes from database

**2. Filtering (10%)**
- **Book filter:** Dropdown to select specific book (0, 1, 2, etc.) or "All Books"
- **Type filter:** Dropdown to select tune type or "All Types"
- Filters should work together (e.g., Book 0 + Type "reel")

**3. Search (5%)**
- Text entry for searching titles
- Search should be case-insensitive
- Search button to execute search

**4. Details Panel (5%)**
- When user clicks a tune in the table, show full details below
- Display: Full title, Alt title (if any), Type, Key
- "View Notation" button opens popup window with full ABC notation

**5. Action Buttons (5%)**
- **Refresh:** Reload data from database
- **Clear:** Clear all filters and show all tunes
- **Export:** Save current filtered results to CSV

---

## Part 4: GitHub Repository (10%)

### Task 4.1: Repository Structure

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

### Task 4.2: README.md Requirements

Your README must include:

```markdown
# ABC Music Database Explorer

## Description
Brief description of the project

## Features
- List key features

## Installation


## Usage
How to use the application with screenshots

## Technologies Used
- Python
- MySQL
- Pandas
- Tkinter

```

### Task 4.3: requirements.txt

```
pandas>=1.5.0
mysql-connector-python>=8.0.0
```

### Task 4.4: Git Best Practices

**Required:**
- Minimum 10 meaningful commits throughout development
- Clear commit messages (not "update" or "fix")
- Use `.gitignore` to exclude:
  - `__pycache__/`
  - `*.pyc`
  - `.env`
  - Personal database credentials
  - Data files (unless small)

**Commit message examples:**
```
✓ "Add database schema and connection code"
✓ "Implement ABC file parser"
✓ "Create tune table with filtering"
✗ "update"
✗ "stuff"
```

---

## Part 5: Documentation & Demo (5%)

### Task 5.1: Code Documentation

- Use docstrings for all functions and classes
- Include type hints where appropriate
- Add comments for complex logic

### Task 5.2: Screenshots

Include in `docs/screenshots/`:
- Main window showing tune list
- Filters in action
- Details panel with selected tune
- Notation popup window

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Database (30%)** | | |
| Schema design | 5 | Correct table structure with indexes |
| File discovery | 5 | Correctly finds all ABC files and book numbers |
| Parsing | 10 | Accurately parses tunes from ABC files |
| Database insertion | 10 | Properly inserts all tunes with correct book numbers |
| **Pandas (15%)** | | |
| Loading data | 5 | Successfully loads from MySQL to DataFrame |
| Analysis functions | 10 | Filter, search, and statistics functions work |
| **GUI (40%)** | | |
| Table display | 10 | Clean, readable Treeview with all columns |
| Filtering | 10 | Book and type filters work correctly |
| Search | 5 | Title search works (case insensitive) |
| Details panel | 5 | Shows selected tune info |
| Notation viewer | 5 | Popup displays full notation |
| Polish | 5 | Professional appearance, error handling |
| **GitHub (10%)** | | |
| Repository structure | 3 | Well-organized with proper folders |
| README | 3 | Complete, clear instructions |
| Git usage | 4 | 10+ meaningful commits, good messages |
| **Documentation (5%)** | | |
| Code comments | 2 | Clear docstrings and comments |
| Screenshots | 1 | Multiple screenshots showing features |
| Demo | 2 | Successful live demonstration |
| **TOTAL** | **100** | |

---

## Submission Requirements

1. **GitHub Repository URL** via the submission link

### Required Technologies
- **Python 3.8+**
- **MySQL 8.0+**
- **pandas**
- **tkinter** (usually included with Python)
- **mysql-connector-python** or **pymysql**

### Optional Enhancements (Bonus)
- Parse the tunes and generate search keys
- Add plot visualizations (matplotlib)
- Implement edit/delete tune functionality
- Add user authentication
- Create playlist/favorites feature
- Export to PDF