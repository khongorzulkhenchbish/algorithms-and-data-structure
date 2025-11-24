import sys
from collections import defaultdict

"""
Problem: Given multiple text files, find the words that appear in at least N of those files.
"""

def get_unique_words_from_file(file_path):
    """
    Opens a file, cleans the text, and returns a SET of unique words 
    found in that specific file.
    """
    words_in_file = set()
    
    try:
        with open(file_path, 'r') as f:
            # Iterate through lines
            # In get_unique_words_from_file
            for line in f:
                line = line.lower()
                # Replace common punctuation with space
                for char in ".,[]":
                    line = line.replace(char, " ")
                
                # Now split (handles multiple spaces automatically)
                for word in line.split():
                    words_in_file.add(word)
            
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return set() # Return empty set on error

    return words_in_file

def build_inverted_index(file_list):
    """
    Reads all files and builds a dictionary mapping:
    Word -> List of Files it appears in
    """
    # Hint: defaultdict(list) is your friend here.
    # Structure: { 'server': ['log_a.txt', 'log_b.txt'], 'failed': [...] }
    word_map = defaultdict(list)

    for file_name in file_list:
        # Get the unique words for this specific file
        unique_words = get_unique_words_from_file(file_name)
        
        # Loop through these unique_words
        for word in unique_words:
            # Update 'word_map' so that the word points to this file_name
            word_map[word].append(file_name)

    return word_map

def print_results(word_map, min_files=2):
    """
    Prints words that appear in at least 'min_files' number of files.
    """
    print(f"--- Words appearing in at least {min_files} files ---")
    
    # Iterate through the word_map
    for word, files in word_map.items():
    # Check if the list of files for that word has length >= min_files
        if len(files) >= min_files:
            # TODO: Print the word and the list of files
            print(f"word: {word} appeared {len(files)} times in files {files}")

# --- Execution ---
if __name__ == "__main__":
    # Test with the files we generated in the previous step
    files = ["commonword/log_a.txt", "commonword/log_b.txt", "commonword/log_c.txt"]
    
    index = build_inverted_index(files)
    print_results(index)