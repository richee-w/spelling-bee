#!/usr/bin/python3
#
#
# GNU General Public License, version 3

import tkinter as tk
from tkinter import messagebox
import random

def generate_words():
    try:
        num_letters = int(num_letters_entry.get())
        num_words = int(num_words_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for number of letters and number of words.")
        return

    if num_letters < 1 or num_words < 1 or num_words > 20:
        messagebox.showerror("Error", "Number of letters must be greater than 0 and number of words must be between 1 and 20.")
        return

    with open("word_list.txt", "r") as f:
        word_list = [word.strip() for word in f.readlines() if len(word.strip()) == num_letters]

    if len(word_list) < num_words:
        messagebox.showerror("Error", "Not enough words with the specified number of letters.")
        return

    words = random.sample(word_list, num_words)
    word_display.configure(text="\n".join(words))

root = tk.Tk()
root.title("Spelling Contest")

num_letters_label = tk.Label(root, text="Number of letters:")
num_letters_label.pack()

num_letters_entry = tk.Entry(root)
num_letters_entry.pack()

num_words_label = tk.Label(root, text="Number of words (max 20):")
num_words_label.pack()

num_words_entry = tk.Entry(root)
num_words_entry.pack()

generate_button = tk.Button(root, text="Generate Words", command=generate_words)
generate_button.pack()

word_display = tk.Label(root, text="")
word_display.pack()

root.mainloop()