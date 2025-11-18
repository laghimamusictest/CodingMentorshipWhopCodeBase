# ==========================================================
# 🐍 PYTHON HOMEWORK: Variables and Strings
# ----------------------------------------------------------
# Instructions:
# Each section below has a short Python script with mistakes.
# Read the comments carefully, fix the errors, and make sure
# your code prints the correct final output as shown.
#
# Do not use "if" statements or "functions".
# Just correct syntax, string usage, and variable logic.
# ==========================================================


# ----------------------------------------------------------
# 1️⃣ Exercise 1: Fix the Quotes
# ----------------------------------------------------------
# The code below should print YouTube.
# Currently, it causes an error because the string is missing quotes.
# Fix the code so the output is:
# Output → YouTube

name = "YouTube"
print(name)


# ----------------------------------------------------------
# 2️⃣ Exercise 2: Add a Space Between Words
# ----------------------------------------------------------
# The code prints "YouTuberocks!" but we want "YouTube rocks!"
# Add a space in the right place using string concatenation.
# Output → YouTube rocks!

platform = "YouTube"
message = " rocks!"
print(platform + message)


# ----------------------------------------------------------
# 3️⃣ Exercise 3: Combine Text and a Variable
# ----------------------------------------------------------
# This causes a TypeError because strings and numbers can’t be added directly.
# Fix it so the output prints:
# Output → Welcome to Python Learners 123

channel = "Python Learners"
print("Welcome to " + channel + str(123))


# ----------------------------------------------------------
# 4️⃣ Exercise 4: Indexing Practice
# ----------------------------------------------------------
# This code tries to access a character that doesn’t exist.
# Change the index so it prints the last letter of "Learning".
# Output → g

word = "Learning"
print(word[7])


# ----------------------------------------------------------
# 5️⃣ Exercise 5: Slice the Word
# ----------------------------------------------------------
# This code prints too many letters.
# Change the slice so it prints only the first three letters of "Programming".
# Output → Pro

text = "Programming"
print(text[0:2])


# ----------------------------------------------------------
# 6️⃣ Exercise 6: Fix the Typo
# ----------------------------------------------------------
# The variable "name" has a spelling error.
# Fix the typo so the output is:
# Output → Welcome to python

name = "python"
print("Welcome to " + name)


# ----------------------------------------------------------
# 7️⃣ Exercise 7: Change a Letter (The Right Way)
# ----------------------------------------------------------
# Strings are immutable, meaning you can’t directly change letters.
# This code causes a TypeError.
# Fix it by building a new string instead.
# Output → Music

title = "music"
title[0] = "M"
print(title[0] + title[1:4])


# ----------------------------------------------------------
# 8️⃣ Exercise 8: Count the Letters
# ----------------------------------------------------------
# Python doesn’t have a function called "length()".
# Use the correct function to count the characters in the word.
# Output → 9

word = "Guitarist"
print(len(word))


# ----------------------------------------------------------
# 9️⃣ Exercise 9: Mix Uppercase and Lowercase
# ----------------------------------------------------------
# Add a space between a and b and fix capitalization.
# Output → Rock music

a = "ROCK"
b = " music"
print(a + b)


# ----------------------------------------------------------
# 🔟 Exercise 10: All Concepts Together
# ----------------------------------------------------------
# Predict what this prints before running it!
# Output → YouT rocks

name = "YouTube"
print(name[0] + name[1:4] + " " + "rocks")
YouTu rocks