#!/usr/bin/python3

import random
import string
import os

def generate_word_list():
    # Open the word list file and read its contents
    with open("word_list.txt", "r") as f:
        words = f.readlines()
    # Return a list of words with any leading/trailing whitespace removed
    return [word.strip() for word in words]

def generate_spelling_competition():
    # Generate the word list
    word_list = generate_word_list()
    sections = []
    # Generate 50 random words for each section of 6-18 letter words
    for i in range(6, 19):
        section_words = [random.choice(word_list) for _ in range(50)]
        sections.append((i, section_words))
    # Generate 30 random words for each section of 19-20 letter words
    for i in range(19, 21):
        section_words = [random.choice(word_list) for _ in range(30)]
        sections.append((i, section_words))
    # Generate 15 random words for each section of 21-22 letter words
    for i in range(21, 23):
        section_words = [random.choice(word_list) for _ in range(15)]
        sections.append((i, section_words))
    # Write the spelling competition document to a file
    with open("spelling_competition.rtf", "w") as f:
        f.write("{\\rtf1\\ansi\n")
        f.write("\\b Spelling Competition\\b0\n")
        for length, words in sections:
            f.write("\\par\n")
            f.write("\\b " + str(length) + "-Letter Words\\b0\n")
            f.write("\\par\n")
            f.write(" ".join(words))
            f.write("\\par\n")
        f.write("}")
    print("Spelling competition document generated successfully!")

# Call the function to generate the spelling competition document
generate_spelling_competition()