from MorseCode import *
# %% test Build_Character_Encoder
Character_Encoder = Build_Character_Encoder()
if Character_Encoder['a'] != '.-':
    print('a is wrong in Character_Encoder')
if Character_Encoder['A'] != '.-':
    print('A is wrong in Character_Encoder')
if Character_Encoder['0'] != '-----':
    print('0 is wrong in Character_Encoder')
if Character_Encoder['!'] != '.-.-.-':
    print('! is wrong in Character_Encoder')
#%% test Build_Character_Decoder




Character_Decoder = Build_Character_Decoder()
if Character_Decoder['.-'] != 'a':
    print('a is wrong in Character_Decoder')
if Character_Decoder['-----'] != '0':
    print('0 is wrong in Character_Decoder')
if Character_Decoder['.-.-.-'] != '#':
    print('# is wrong in Character_Decoder')
#%% test Word_Encoder
print('gin:', Word_Encoder('gin'))
print('zen', Word_Encoder('zen'))
print('gig', Word_Encoder('gig'))
print('msg', Word_Encoder('msg'))
if Word_Encoder('gin') == Word_Encoder('zen'):
    print('0: wrong in Word_Encoder')
if Word_Encoder('gig') == Word_Encoder('msg'):
    print('1: wrong in Word_Encoder')
#%% some examples for testing Message_Encoder and Message_Decoder
test_cases=[['python is great', 
            '.--. -.-- - .... --- -.,.. ...,--. .-. . .- -'], 
            ['python is easy',
            '.--. -.-- - .... --- -.,.. ...,. .- ... -.--'],
            ['python is powerful',
             '.--. -.-- - .... --- -.,.. ...,.--. --- .-- . .-. ..-. ..- .-..'],  
            ['the quick brown fox jumps over the lazy dog 0 1 2 3 4 5 6 7 8 9',
             '- .... .,--.- ..- .. -.-. -.-,-... .-. --- .-- -.,..-. --- -..-,.--- ..- -- .--. ...,--- ...- . .-.,- .... .,.-.. .- --.. -.--,-.. --- --.,-----,.----,..---,...--,....-,.....,-....,--...,---..,----.']]
try:
    for n in range(0, len(test_cases)):    
        M=test_cases[n][0]
        C=test_cases[n][1]
        C_ = Message_Encoder(M)
        M_ = Message_Decoder(C)
        if C != C_:
            print('something is wrong in Message_Encoder')
            print('you get zero score')
            break
        if M != M_:
            print('something is wrong in Message_Decoder')
            print('you get zero score')
            break
except:
    print('you get zero score for the lab')
#%%
print('If your code passes the test, it does not mean it has no bugs.')