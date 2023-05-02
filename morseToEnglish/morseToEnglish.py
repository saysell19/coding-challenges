# A program that converts Morse code to English text and English text to Morse code. 
 
class MorseTranslator:
    def __init__(self):

        self.morse_code_dictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '
        }

    def encrypt(self, message):

        # Translates English to Morse Code
        #     Uses the .join method that loops over the provided 'message' which is formatted to UPPERCASE
        #      and adds the Value(morse) of each Key(message char) to the string
        #     finally returning 'message' in morse code
        return " ".join(self.morse_code_dictionary[char] for char in message.upper())
    

    def decrypt(self, message):
        # Translates Morse Code to English
        # Variables are declared to hold the message, dicipered message and capture the morse code (for any given letter)
        message += " "
        decipher = ""
        citext = ""

        # Loops over the message and checks if the letter is not whitespace
        for letter in message:
            if letter != " ":
                # "i" is used to count the number of spaces
                i = 0
                citext += letter
            # If the letter is a whitespace, then it checks if the letter is space (again and then it will +1 to"i") or a letter
            else:
                i += 1
                # If more than one char is whitespace then it adds a space to the deciphered message, as this will be a new word
                if i == 2:
                    decipher += " "
                # If the letter is not a space, then the morse code (within "citext") is equated 
                # against the VALUE (within "morse_code_dictionary") in which case;
                # the KEY is added to the "decipher" message, as this will be the correct char of the translated word
                else:
                    # Loops over the morse code dictionary and checks if the morse code within "citest" is equal to the letter
                    for key, value in self.morse_code_dictionary.items():
                        if citext == value:
                            decipher += key
                    # Resets the citext to empty string
                    citext = ""
        # Returns the deciphered message
        return decipher

    
translate = MorseTranslator()
# print(translate.encrypt('HELLO WORLD'))
# print(translate.decrypt('.... . .-.. .-.. ---   .-- --- .-. .-.. -..'))


if __name__ == '__main__':
    print("""This program converts Morse code to English text and English text to Morse code. \n 
        You will be asked to enter a message to be converted. \n
        It will take your input and conver it to MORSE CODE. \n 
        Then it will convert it back to ENGLISH""")
    message = input("Enter a message to be converted: ")
    print(translate.encrypt(message))

    print(f"Your message in morse code is: {translate.encrypt(message)}")
    print(f"Your message in english is: {translate.decrypt(translate.encrypt(message))}")

    