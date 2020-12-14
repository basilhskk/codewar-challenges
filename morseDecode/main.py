# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python
def decodeMorse(morse_code):
    CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', 
        
        
        "[SPACE]":"",
            
        "SOS":"...---...",
        "!":"-.-.--",
        ".":".-.-.-"
        }

    morse_word = morse_code.split(" ")
    print(morse_word)
    word = ""
    for i in range(len(morse_word)):
        for letter,value in CODE.items():
            if morse_word[i] == value:
                word = word + letter

    word = word.replace("[SPACE][SPACE][SPACE]","")
    word = word.replace("[SPACE][SPACE]"," ")
    word = word.replace("[SPACE]","").strip()
    return word

decodeMorse('.... . -.--     .--- ..- -.. .  ')