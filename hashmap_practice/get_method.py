# A more concise way (use get() method):
# color_dict.get(color, 0): This part checks if color is already a key in color_dict. If it is, it returns its current value. If not, it returns 0.

# Function to count the frequency of each letter in a given sentence
def count_letter_frequency(sentence):
    letter_count = {}
    for letter in sentence:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
        # If the character is a letter, update its count in the dictionary
        # or add it with a count of 1 if it's not already there
    return letter_count

# Example usage with a predefined sentence
sentence = "Once upon a time in a faraway library"
# TODO: Call the function with the sentence variable and print the result
print(count_letter_frequency(sentence))