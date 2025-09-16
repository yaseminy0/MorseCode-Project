def Build_Character_Encoder():
    # CodeList1 contains Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # CodeList2 contains Morse codes of the 10 integers from 0 to 9
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')
    CharList3 = list("""`~!@#$%^&*()-_=+[{]}\\|;:'",<.>/?""")
    
    # Initialize the dictionary
    Character_Encoder = {}
    
    # LETTERS (lowercase):
    for c, code in zip(CharList1, CodeList1):
        Character_Encoder[c] = code
    
    # LETTERS (uppercase) - same morse code as lowercase:
    for c, code in zip(CharList1, CodeList1):
        Character_Encoder[c.upper()] = code
        
    # NUMBERS:
    for c, code in zip(CharList2, CodeList2):
        Character_Encoder[c] = code

    # SPECIAL CHARACTERS:
    for s in CharList3:
        Character_Encoder[s] = '.-.-.-'
    
    # Return the dictionary
    return Character_Encoder



    
def Build_Character_Decoder():
    # Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # Morse codes of the 10 integers from 0 to 9
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')

    Character_Decoder = {}

    # letters (always lowercase)
    for c, code in zip(CharList1, CodeList1):
        Character_Decoder[code] = c

    # digits
    for c, code in zip(CharList2, CodeList2):
        Character_Decoder[code] = c

    # special characters (all map to '#')
    Character_Decoder['.-.-.-'] = '#'

    return Character_Decoder


def Word_Encoder(Word, Character_Encoder=None):
    
    if Character_Encoder is None:
        Character_Encoder=Build_Character_Encoder()
    codes = []
    for ch in Word:
        code = Character_Encoder.get(ch,'.-.-.-')
        codes.append(code)
    Word_in_Morse_Code = ' '.join(codes)
    return Word_in_Morse_Code


def Word_Decoder(Word_in_Morse_Code, Character_Decoder=None):
    if Character_Decoder is None:
        Character_Decoder = Build_Character_Decoder()

    chars = []
    for code in Word_in_Morse_Code.split():
        ch = Character_Decoder.get(code, '#')
        chars.append(ch)

    Word = ''.join(chars)
    return Word



def Message_Encoder(Message, Character_Encoder=None):
    if Character_Encoder is None:
        Character_Encoder = Build_Character_Encoder()

    words = Message.split()  
    codes = []
    for w in words:
        codes.append(Word_Encoder(w, Character_Encoder))

    
    Message_in_Morse_Code = ','.join(codes)
    return Message_in_Morse_Code


def Message_Decoder(Message_in_Morse_Code, Character_Decoder=None):
    if Character_Decoder is None:
        Character_Decoder = Build_Character_Decoder()

    word_codes = Message_in_Morse_Code.split(',')  
    words = []
    for wc in word_codes:
        words.append(Word_Decoder(wc, Character_Decoder))

    Message = ' '.join(words)
    return Message
