import sys

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
    else:
        print("Word is too long. Please enter a word with less than 21 letters.")
    count = letters - sub
    return count
    

#python TextRedacter.py <input_file> <output_file> <word_to_redact> <redacted_word>
# Check for correct number of arguments
def Redact(input_file, output_file, word_to_redact):
    file = open(input_file, "r")
    output = open(output_file, "w")
    if (word_to_redact == 'pro_nouns'): #redact all pronouns
        for line in file:
            for word in line.split():  #go word by word
                if word in pro_nouns:
                    line = line.replace(word, "X" * count_X(word))
            output.write(line)
    else: #redact a specific word
        redacted_word = "X" * count_X(word_to_redact)
        for line in file:
            if (word_to_redact in line):
                output.write(line.replace(word_to_redact, redacted_word))
            else:
                output.write(line)
    file.close()
    output.close()

pro_nouns = ['she', 'She', 'Her','her', 'Hers', 'hers', 'He', 'he', 'Him', 'him', 'His', 'his'] #list of pronouns
if ((len(sys.argv) == 2) and (sys.argv[1] == '-help')):
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Sample use: python TextRedacter.py <input_file> <output_file> <word_to_redact>\n\nReplace <input_file> with the name of the file you want to redact.\n\nReplace <output_file> with the name of the file you want to write the redacted text to.\n\nReplace <word_to_redact> with the word you want to redact.\n\nNote: You can pass pro_nouns as the <word_to_redact> to redact all pronouns.\nExample: python TextRedacter.py input.txt output.txt pro_nouns")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
elif (len(sys.argv) != 4):
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    print("Incorrect number of arguments. Please enter 4 arguments.\n\nSample use: python TextRedacter.py <input_file> <output_file> <word_to_redact>\n\nHelp: python TextRedacter.py -help")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
else:
    Redact(sys.argv[1], sys.argv[2], sys.argv[3])

