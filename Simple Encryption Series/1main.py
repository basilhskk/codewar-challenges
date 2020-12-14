def decrypt(encrypted_text, n):
    if n <= 0 :
        return encrypted_text


def encrypt(text, n):
    if n <= 0 :
        return text

    text = list(text)
    secondChars =[]
    
    for i in range(0,len(text),2):
        secondChars.append(text[i])
        
    print(secondChars)

encrypt("This is a test!", 1)

# encrypt("This is a test!", 1), "hsi  etTi sats!"
# encrypt("This is a test!", 0), "This is a test!"
# decrypt("This is a test!", 0), "This is a test!"
# encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig"
# decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!"