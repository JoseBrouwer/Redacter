# Redacter
- This is a simple text redaction program that takes a text file as input and replaces key words with a redacted version.
- The program takes 4 arguments: the input file, the output file, the word to redact, and the redacted word.
- The program will replace the word to redact with the redacted word in the output file.
- If the word to redact is "pro_nouns", then the program will redact all pronouns in the input file.
- This is achieved through the use of regular expressions and simple pattern recognition (in the form of the count_X function to determine the right amount of Xs to use to maintain formatting as much as possible.) to find specific words and replace them in a copy of the document. 
- use the command python3 TextRedacter.py -help for assistance with use. 
- Sample use: python3 TextRedacter.py <input_file> <output_file> <word_to_redact> 
    - Replace files with their absolute paths to ensure proper functionality
    - <word_to_redact> can be replaced with "pro_nouns" to remove all of the pronouns in the document. 
- Make sure to replace program path in batch file to run from Windows Run Terminal. 