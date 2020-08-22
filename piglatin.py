INP_STR  = input("Enter a sentence: ")  # Get input string from user
WORD     = ''   # Initiating the first word
WD_COUNT = 0    # Initiating the word count
OUT_STR  = ''   # Initiating the output string
for INDEX in range(len(INP_STR)):   # Process every character in input string
    # Determine end of word based on the terminal characters , !?.:;
    if INP_STR[INDEX] in [',', ' ', '!', '?', '.', ':', ';']:
        if  len(WORD) > 0:
            WD_COUNT = WD_COUNT + 1  # Increment word count for every word
            if  WORD[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                # Add 'yay' to end of the word that starts with a vowel
                OUT_STR = OUT_STR + WORD + 'yay'
            else:
                # Add 'ay' to end of the word that doesn't starts with a vowel
                OUT_STR = OUT_STR + WORD[1:len(WORD)] + WORD[0] + 'ay'
        # Do this even when WORD length is zero or more
        OUT_STR = OUT_STR + INP_STR[INDEX]
        WORD = ''   # Re-initiating WORD to capture the next word
    else:
        WORD = WORD + INP_STR[INDEX]    # Adding characters to WORD

# Though the last WORD is captured, it is not yet processed \
# to be part of the output string
# Process the last word if the word doesn't end with either of , !?.:;
if len(WORD) > 0:
    WD_COUNT = WD_COUNT + 1  # Increment word count for the last word
    if  WORD[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        # Add 'yay' to end of the word that starts with a vowel
        OUT_STR = OUT_STR + WORD + 'yay'
    else:
        # Add 'ay' to end of the word that doesn't starts with a vowel
        OUT_STR = OUT_STR + WORD[1:len(WORD)] + WORD[0] + 'ay'

print(f'Words: {WD_COUNT}')
print(f'PigLatin Translation of your sentence is : "{OUT_STR}"')
exit()
