# Redacter
Text Redacter
This is a simple text redaction program that takes a text file as input and replaces key words with a redacted version.
The program takes 4 arguments: the input file, the output file, the word to redact, and the redacted word.
The program will replace the word to redact with the redacted word in the output file.
If the word to redact is pro_nouns, then the program will redact all pronouns in the input file.
The program will also redact the word to redact if it is a substring of a word in the input file. Want it to just be whole words.
Currently creates a new file but this is for testing purposes and will be changed to overwrite the input file