#!/usr/bin/python3
# GNU General Public License, version 3

import random
import string
import os

def generate_word_list():
    try:
        # Open the word list file and read its contents
        with open("word_list.txt", "r") as f:
            words = f.readlines()
        # Return a list of words with any leading/trailing whitespace removed
        return [word.strip() for word in words]
    except Exception as e:
        print("An error occurred while reading the word list: ", e)
        return []

def generate_spelling_competition():
    try:
        # Generate the word list
        word_list = generate_word_list()
        sections = []

        # Prepare dictionary with word lengths as keys and words as values
        word_dict = {i: [word for word in word_list if len(word) == i] for i in range(6, 23)}

        # Generate words for each section without duplicates and checking for empty list
        for i in range(6, 19):
            section_words = random.sample(word_dict[i], min(50, len(word_dict[i]))) if len(word_dict[i]) > 0 else []
            sections.append((i, section_words))

        for i in range(19, 21):
            section_words = random.sample(word_dict[i], min(30, len(word_dict[i]))) if len(word_dict[i]) > 0 else []
            sections.append((i, section_words))

        for i in range(21, 23):
            section_words = random.sample(word_dict[i], min(15, len(word_dict[i]))) if len(word_dict[i]) > 0 else []
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

    except Exception as e:
        print("An error occurred during the generation of the spelling competition: ", e)


# Call the function to generate the spelling competition document
generate_spelling_competition()
