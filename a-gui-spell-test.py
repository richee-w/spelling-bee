#!/usr/bin/python3
#
#
# GNU General Public License, version 3

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

def generate_words():
    try:
        num_letters = int(num_letters_entry.get())
        num_words = int(num_words_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for number of letters and number of words.")
        return

    if num_letters < 1 or num_words < 1 or num_words > 50:
        messagebox.showerror("Error", "Number of letters must be greater than 0 and number of words must be between 1 and 50.")
        return

    with open("word_list.txt", "r") as f:
        word_list = [word.strip() for word in f.readlines() if len(word.strip()) == num_letters]

    if len(word_list) < num_words:
        if len(word_list) == 0:
            messagebox.showerror("Error", f"No words with {num_letters} letters found in the dictionary.")
        else:
            messagebox.showwarning("Warning", f"Not enough words with {num_letters} letters in the dictionary. Maximum number of words available: {len(word_list)}")
        return

    words = random.sample(word_list, num_words)

    # Split words into three columns
    col1 = words[:num_words//3]
    col2 = words[num_words//3:(num_words//3)*2]
    col3 = words[(num_words//3)*2:]

    # Clear previous output
    word_display.delete(*word_display.get_children())

    # Insert new output
    for i in range(max(len(col1), len(col2), len(col3))):
        word_display.insert("", tk.END, text=col1[i] if i < len(col1) else "", values=(col2[i] if i < len(col2) else "", col3[i] if i < len(col3) else ""))


    # Insert new output
    for i, word in enumerate(words):
        word_display.insert("", tk.END, text=str(i+1), values=(word,))

root = tk.Tk()
root.title("Spelling Contest")

# Number of letters entry
num_letters_label = tk.Label(root, text="Number of letters:")
num_letters_label.grid(row=0, column=0)

num_letters_entry = tk.Entry(root, width=10)
num_letters_entry.grid(row=0, column=1)

# Number of words entry
num_words_label = tk.Label(root, text="Number of words (max 50):")
num_words_label.grid(row=1, column=0)

num_words_entry = tk.Entry(root, width=10)
num_words_entry.grid(row=1, column=1)

# Generate button
generate_button = tk.Button(root, text="Generate Words", command=generate_words)
generate_button.grid(row=2, column=1)

# Word display
word_display = tk.ttk.Treeview(root, columns=("column1", "column2"))
word_display.heading("#0", text="No.")
word_display.heading("#1", text="Words")
word_display.column("#0", width=50)
word_display.column("#1", width=200)
word_display.grid(row=3, columnspan=2)

root.mainloop()
