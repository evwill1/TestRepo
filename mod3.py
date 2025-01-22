# enter and print sentence
sentence = "Code never lies, comments sometimes do"
print(sentence)

# Calculate the length of the string
length = len(sentence)
print(f"calculating above string length: {length}")

# Add a new line after the comma
new_line = sentence.replace(",", "\n")

# Print the result
print("Modified string with a new line after the comma:")
print(new_line)

# capitalize all characters in string
capitalized = sentence.upper()
print(capitalized)

# Slice "Code never lies" out of the string and concatenate the length of this substring on the end of it
sliced = sentence[0:15]
length = len(sliced)
print(f"Sliced text and length: {sliced}, {length}")