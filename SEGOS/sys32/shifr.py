def encrypt(text):
    output1 = '';offset = 5
    for x in text:
        if (ord(x) + offset > 126):
            letter = (ord(x) + offset) - 95
            output1 = output1 + chr(letter)
        else:
            letter = ord(x) + offset
            output1 = output1 + chr(letter)
    return output1

def decrypt(text):
    output2 = '';offset = 5
    for y in text:
        if (ord(y) - offset > 126):
            letter = (ord(y) - offset) - 95
            output2 = output2 + chr(letter)
        else:
            letter = ord(y) - offset
            output2 = output2 + chr(letter) 
    return output2