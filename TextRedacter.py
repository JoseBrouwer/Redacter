import re
import sys

def count_X(string):
    letters = len(string)
    if letters <= 5:
        sub = 1
    elif letters <= 10:
        sub = 2
    elif letters <= 15:
        sub = 3
    elif letters <= 20:
        sub = 4
    else:
        raise ValueError("Word is too long. Please enter a word with less than 21 letters.")
    count = letters - sub
    return count

def redact_text(input_file, output_file, word_to_redact):
    with open(input_file, "r") as file:
        text = file.read()

    if word_to_redact == 'pro_nouns':  # redact all pronouns
        pronouns = ['she', 'She', 'Her', 'her', 'Hers', 'hers', 'He', 'he', 'Him', 'him', 'His', 'his']
        for pronoun in pronouns:
            word_regex = r'\b{}\b'.format(re.escape(pronoun))
            text = re.sub(word_regex, "X" * count_X(pronoun), text)
    else:  # redact a specific word
        word_regex = r'\b{}\b'.format(re.escape(word_to_redact))
        text = re.sub(word_regex, "X" * count_X(word_to_redact), text)

    with open(output_file, "w") as file:
        file.write(text)

    print("Text redaction complete.")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Sample use: python3 TextRedacter.py <input_file> <output_file> <word_to_redact>\n\nReplace <input_file> with the name of the file you want to redact.\n\nReplace <output_file> with the name of the file you want to write the redacted text to.\n\nReplace <word_to_redact> with the word you want to redact.\n\nNote: You can pass pro_nouns as the <word_to_redact> to redact all pronouns.\nExample: python TextRedacter.py input.txt output.txt pro_nouns")
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    elif len(sys.argv) != 4:
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
        print("Incorrect number of arguments. Please enter 4 arguments.\n\nSample use: python3 TextRedacter.py <input_file> <output_file> <word_to_redact>\n\nHelp: python TextRedacter.py -help")
        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------\n")
    else:
        redact_text(sys.argv[1], sys.argv[2], sys.argv[3])
