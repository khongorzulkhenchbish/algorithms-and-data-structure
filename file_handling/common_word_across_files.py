import sys
import re

"""
Problem: Given multiple text files, find the words that are common across all files.
File Handling
The key function for working with files in Python is the open(), it takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists


s = "...hello, world;;"
print(s.strip(".,:;"))  # "hello, world"
"""
def file_to_wordset(path):
    word_set = set()

    try:
        with open(path, "r") as file:
            # NOTE: Even if the file is 10GB, we only store the unique words in memory, not the raw text.
            # In get_unique_words_from_file
            for line in file:
                line = line.lower()
                # Replace common punctuation with space
                for char in ".,[]":
                    line = line.replace(char, " ")
                
                # Now split (handles multiple spaces automatically)
                for word in line.split():
                    word_set.add(word)

    except FileNotFoundError:
        print(f"File: {path} not found.")
        return None

    return word_set

def find_common_words(paths):
    # go through each file and store the sets
    if len(paths) == 0:
        return []

    # initialize the common words set with the first file's words
    common_words = file_to_wordset(paths[0])

    # if the first file is not found, return empty list
    if common_words is None:
        return []

    # do the same but for the rest of the files
    for path in paths[1:]:
        # using with closes the file automatically
        current_words = file_to_wordset(path)
        
        if current_words:
            # Using set.intersection is $O(N)$ (average case) and much faster than nested loops
            common_words = common_words.intersection(current_words)
            # Optimization: If common_set becomes empty, we can stop early!
            # If the first two files have nothing in common, there is no point reading the third file.
            if not common_words:
                break # this will return empty common_words list
        else:
            # if any file is not found or current_words is already empty, then return empty list
            return []

    return list(common_words)



if __name__ == "__main__":
    # In the real interview, you might get these from sys.argv
    files = ["commonword/log_a.txt", "commonword/log_b.txt", "commonword/log_c.txt"]
    
    # Run the function
    result = find_common_words(files)
    
    # "server" appears in all 3 (but with different casing/punctuation).
    # "failed" appears in all 3.
    # "timeout" appears in only 2 files (should not be in the result).
    with open("commonword/common_words.txt", "w") as output_file:
        output_file.write(f"Common words are:\n{result}")