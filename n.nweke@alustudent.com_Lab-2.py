#!/usr/bin/python3

# First we need to read the contents of the two files we are comparing
with open('essay1.txt') as essay1_file:
    essay1_content = essay1_file.read().lower().split()
    essay1_words = []
    for word in essay1_content:
        if word.isalnum():
            essay1_words.append(word)

with open('essay2.txt') as essay2_file:
    essay2_content = essay2_file.read().lower().split()
    essay2_words = []
    for word in essay2_content:
        if word.isalnum():
            essay2_words.append(word)

# Finding Common Words in both essays
common_words = {}
for word in set(essay1_words).intersection(set(essay2_words)):
    common_words[word] = min(essay1_words.count(word), essay2_words.count(word))

plagiarised_words = len(common_words)

# Total unique words
total_unique_words = len(set(essay1_words).union(set(essay2_words)))

# Calculation for Plagiarism Percentage
plagiarism_percentage = (plagiarised_words / total_unique_words) * 100 if total_unique_words > 0 else 0  # Avoid division by zero

# Function to search for specific word in both essays
def search_word(word, essay_words):
    return word in essay_words

# Displaying the plagiarism result conditionally
if plagiarism_percentage > 50:
    print(f"You plagiarism percentage is {plagiarism_percentage}%, so you plagiarised for sure buddy. Book office hour with me.")
    print(" ")
else:
    print(f"Your plagiarism percentage is {plagiarism_percentage}%, so you didn't plagiarised for sure buddy. Great job!!")
    print(" ")

# Display common words
print("Common words found in both essays with their counts:\n", common_words)
print(" ")

print("Do you want to search for a specific word in either of the essays?")
print("Enter 'Y' for Yes:")
print("Enter 'N' for No to quit:")
search_for_word = input("Enter your response: ").lower()

if search_for_word != 'y' and search_for_word != 'n':
    print("Enter a valid response!")
    search_for_word = input("Enter your response: ").lower()

if search_for_word == "y":
    print("Which essay do you want to search in?")
    print("Enter '1' for essay1.txt")
    print("Enter '2' for essay2.txt")
    essay_choice = input("Enter your choice: ")

    if essay_choice == '1':
        word_to_search = input("Enter the word you want to search for in essay1: ")
        print(search_word(word_to_search, essay1_words))
    elif essay_choice == '2':
        word_to_search = input("Enter the word you want to search for in essay2: ")
        print(search_word(word_to_search, essay2_words))
    else:
        print("Invalid choice. Please select either '1' or '2'.")
else:
    print("See you some other time buddy!!")

# Programming Concepts Used:
# - Data structures (e.g., lists, dictionaries)
# - Loops (e.g., for loops)
# - Conditional statements (e.g., if-else statements)
# - Functions (e.g., defining and calling functions)
# - File handling (e.g., reading from files)
