import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_dataframe(df, parent):
    # Create Treeview
    tree = ttk.Treeview(parent)
    tree.pack(fill=tk.BOTH, expand=True)
    
    # Add scrollbars
    vsb = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    
    hsb = ttk.Scrollbar(parent, orient="horizontal", command=tree.xview)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    # Define columns
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"  # Hide the first empty column
    
    # Format columns
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    
    # Add data
    for idx, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))
    
    return tree

# Example usage
root = tk.Tk()
root.title("Pandas DataFrame Viewer")
root.geometry("800x400")

# Sample DataFrame
df = pd.read_csv("data/tuneindex.csv")

display_dataframe(df, root)
root.mainloop()