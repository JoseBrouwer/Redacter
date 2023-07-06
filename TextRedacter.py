import sys

# This is a simple text redaction program that takes a text file as input and replaces key words with a redacted version.

"""
This function counts the number of X's to be used in the redacted word. The pattern follows that if the word has 5 letters or less, then the redacted word will have 1 X. If the word has 6-10 letters, then the redacted word will have 2 X's. If the word has 11-15 letters, then the redacted word will have 3 X's. If the word has 16-20 letters, then the redacted word will have 4 X's. If the word has 21 or more letters, then the redacted word will have 5 X's.
"""
def count_X(string):
    letters = len(string)
    range = letters/5
    sub = 0
    if (range <= 1):
        sub = 1
    elif (range > 1 and range <= 2): 
        sub = 2
    elif (range > 2 and range <= 3):
        sub = 3
    elif (range > 3 and range <= 4):
        sub = 4
    count = letters - sub
    return count
    

#python TextRedacter.py <input_file> <output_file> <word_to_redact> <redacted_word>
# Check for correct number of arguments
def Redact(input_file, output_file, word_to_redact):
    if (len(sys.argv) != 4):
        print("Incorrect number of arguments. Please enter 4 arguments.")
    else:
        file = open(input_file, "r")
        output = open(output_file, "w")
        redacted_word = "X" * count_X(word_to_redact)
        for line in file:
            if (word_to_redact in line):
                output.write(line.replace(word_to_redact, redacted_word))
            else:
                output.write(line)
        file.close()
        output.close()

Redact(sys.argv[1], sys.argv[2], sys.argv[3])

